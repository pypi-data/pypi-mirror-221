# imports
import pandas
import feather
from sklearn.model_selection import train_test_split, KFold, GroupShuffleSplit
import numpy


def split_data(upstream, product, split_type, test_size=0.5, n_folds=10, grouping_variable=None, temporal_split=None):
    # load data from upstream process
    X = feather.read_dataframe(upstream['preprocess_data']['X_data'])
    y = feather.read_dataframe(upstream['preprocess_data']['y_data'])

    # parse split_type parameter
    if split_type == 'train_test':
        # split data
        if grouping_variable is None:
            X_train, X_test, y_train, y_test = train_test_split(
                X, 
                y, 
                test_size=test_size
            )
        else:
            gss = GroupShuffleSplit(
                n_splits=1,
                train_size=1-test_size,
            )
            for train_idx, test_idx in gss.split(X, y, X[grouping_variable]):
                X_train = X.iloc[train_idx]
                y_train = y.iloc[train_idx]
                X_test = X.iloc[test_idx]
                y_test = y.iloc[test_idx]
                if temporal_split:
                    temp_var = temporal_split['temporal_variable']
                    # allocate memory for supplementary training data
                    y_train_sup = y_test.copy()
                    # split each time series 
                    for var in X_test[grouping_variable].unique():
                        # determine the test size
                        if isinstance(temporal_split['test_size'], float):
                            test_prop = temporal_split['test_size']
                        else:
                            test_prop = numpy.random.uniform(
                                min(temporal_split['test_size']),
                                max(temporal_split['test_size'])
                            )
                        max_timestep = X_test.loc[X_test[grouping_variable] == var, temp_var].max()
                        min_timestep = X_test.loc[X_test[grouping_variable] == var, temp_var].min()
                        split_timestep = (max_timestep - min_timestep) * (1 - test_prop)
                        y_train_sup.loc[(X_test[grouping_variable] == var) & (X_test[temp_var] > split_timestep)] = numpy.nan
                        y_test.loc[(X_test[grouping_variable] == var) & (X_test[temp_var] <= split_timestep)] = numpy.nan
                    # add supplementary training data back into training set
                    X_train = pandas.concat([X_train, X_test])
                    y_train = pandas.concat([y_train, y_train_sup])
        # print metadata
        print(f'X_train shape: {X_train.shape}')
        print(f'X_test shape: {X_test.shape}')
        print(f'y_train shape: {y_train.shape}')
        print(f'y_test shape: {y_test.shape}')
        # save data for next process
        feather.write_dataframe(X_train, product['train_X_data'])
        feather.write_dataframe(X_test, product['test_X_data'])
        feather.write_dataframe(y_train, product['train_y_data'])
        feather.write_dataframe(y_test, product['test_y_data'])
    elif split_type == 'k_fold':
        if grouping_variable is not None:
            groups = X[grouping_variable]
        else:
            groups = None
        kfolds = KFold(n_splits=n_folds)
        for i, (train_idx, test_idx) in enumerate(kfolds.split(X, groups=groups)):
            # split data
            fold_X_data = X.iloc[test_idx]
            fold_y_data = y.iloc[test_idx]
            # print metadata
            print(f'Fold {i+1} X shape: {fold_X_data.shape}')        
            print(f'Fold {i+1} y shape: {fold_y_data.shape}')
            # save data for next process   
            feather.write_dataframe(fold_X_data, product[f'fold_{i+1}_X_data'])   
            feather.write_dataframe(fold_y_data, product[f'fold_{i+1}_y_data'])


def temp_split(X_test, y_test, temp_var, group_var, test_size):
    '''
    Split each time series.
    '''
