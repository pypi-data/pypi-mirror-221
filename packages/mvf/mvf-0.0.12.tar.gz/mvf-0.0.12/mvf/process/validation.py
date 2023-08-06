import os
import feather
import pandas
from IPython.display import display
import pickle
import sklearn.metrics


def load_validation_data(upstream, split_type, n_folds=10):
    '''
    Loads validation data from upstream 'split_data' process.
    '''
    if split_type == 'train_test':
        validation_data = feather.read_dataframe(
            upstream['split_data']['test_y_data']
        ).reset_index(drop=True)

    elif split_type == 'k_fold':
        validation_data = []
        for i in range(1, n_folds+1):
            validation_data.append(
                feather.read_dataframe(
                    upstream['split_data'][f'fold_{i}_y_data'])
            )
        validation_data = pandas.concat(validation_data).reset_index(drop=True)
    return validation_data


def load_predictions(upstream, models):
    '''
    Loads predictions from upstream 'predict_model' processes.
    '''
    predictions = {}
    for model_name in models:
        predictions[model_name] = feather.read_dataframe(
            upstream[f'{model_name}_predict']['predictions']
        ).reset_index(drop=True)
    return predictions


def error_metrics(target_features, predictions, validation_data):
    '''
    Calculates error metrics for each of the target features and for each model
    '''
    for target in target_features:
        # error
        error_df = pandas.DataFrame()
        # mse
        for model, preds in predictions.items():
            mean_preds = preds[[target]].add_suffix('_pred', axis=1)
            ground_truth = validation_data[[
                target]].add_suffix('_truth', axis=1)
            # drop null validation values
            merged = pandas.concat([ground_truth, mean_preds], axis=1).dropna(
                subset=f'{target}_truth')

            error_df.loc[model, 'MSE'] = sklearn.metrics.mean_squared_error(
                merged[f'{target}_truth'],
                merged[f'{target}_pred']
            )
            error_df.loc[model, 'RMSE'] = sklearn.metrics.mean_squared_error(
                merged[f'{target}_truth'],
                merged[f'{target}_pred'],
                squared=False
            )
            error_df.loc[model, 'MAE'] = sklearn.metrics.mean_absolute_error(
                merged[f'{target}_truth'],
                merged[f'{target}_pred']
            )
            error_df.loc[model, 'MAPE'] = sklearn.metrics.mean_absolute_percentage_error(
                merged[f'{target}_truth'],
                merged[f'{target}_pred']
            )
            error_df.loc[model, 'R-squared'] = sklearn.metrics.r2_score(
                merged[f'{target}_truth'],
                merged[f'{target}_pred']
            )
        print(f'Error metrics for `{target}` predictions:')
        display(error_df)


def qi_coverage(validation_data, target_features, predictions, quantile_intervals=[]):
    '''
    Calculates the coverage of for each quantile interval, for each target feature. 
    '''
    if quantile_intervals == []:
        print('No quantile intervals specified. Nothing to calculate.')
        return
    for target in target_features:
        qi_coverage = pandas.DataFrame()
        idx = 0
        for model, preds in predictions.items():
            for qi in quantile_intervals:
                lb = f'{target}_Q{min(qi) * 100:g}'
                ub = f'{target}_Q{max(qi) * 100:g}'
                if lb in preds.columns and ub in preds.columns:
                    qi_coverage.loc[idx, 'model'] = model
                    qi_coverage.loc[idx, 'interval'] = str(sorted(qi))
                    qi_coverage.loc[idx, 'level'] = max(qi) - min(qi)
                    # boolean array for qi covering ground truth
                    in_interval = (preds.loc[:, ub] >= validation_data.loc[:, target]) & (
                        preds.loc[:, lb] <= validation_data.loc[:, target])
                    qi_coverage.loc[idx, 'coverage'] = in_interval.sum(
                    ) / in_interval.shape[0]
                    idx += 1
        print(f'Coverage metrics for `{target}` predictions:')
        display(qi_coverage.set_index(['model', 'interval']))


def qi_sharpness(target_features, predictions, quantile_intervals):
    '''
    Calculates the sharpness of each quantile interval for each target feature.
    '''
    if quantile_intervals == []:
        print('No quantile intervals specified. Nothing to calculate.')
        return
    for target in target_features:
        qi_sharpness = pandas.DataFrame()
        for model, preds in predictions.items():
            for qi in quantile_intervals:
                lb = f'{target}_Q{min(qi) * 100:g}'
                ub = f'{target}_Q{max(qi) * 100:g}'
                if lb in preds.columns and ub in preds.columns:
                    qi_sharpness.loc[model, str(sorted(qi))] = (
                        preds[ub] - preds[lb]).mean()
        print(f'Sharpness metrics for `{target}` predictions:')
        display(qi_sharpness)


def computational_performance(upstream, models, split_type, n_folds=10):
    '''
    Calculates computational performance metrics for each model.
    '''
    # computational performance
    comp_perf = pandas.DataFrame()
    for model in models:
        # fit time
        with open(upstream[f'{model}_fit']['process_metadata'], 'rb') as f:
            fit_metadata = pickle.load(f)
        comp_perf.loc[model, 'fit time'] = fit_metadata[f'{model}_fit']
        # predict time
        with open(upstream[f'{model}_predict']['process_metadata'], 'rb') as f:
            predict_metadata = pickle.load(f)
        comp_perf.loc[model,
                      'predict time'] = predict_metadata[f'{model}_predict']
        # model size
        if split_type == 'train_test':
            # only one model
            comp_perf.loc[model, 'size'] = os.path.getsize(
                os.path.join(
                    'output',
                    'models',
                    f'{model}_fit'
                )
            )
        elif split_type == 'k_fold':
            # sum the model sizes
            total_size = 0
            for i in range(1, n_folds+1):
                total_size += os.path.getsize(
                    os.path.join(
                        'output',
                        'models',
                        f'{model}_fit_{i}'
                    )
                )
            comp_perf.loc[model, 'size'] = total_size
    display(comp_perf)
