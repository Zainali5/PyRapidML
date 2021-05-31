
# Author: Zain Ali <zainbalouch3@gmail.com>
# License: MIT
# Release: PyRapidML
# Last modified : 31/05/2021

import pandas as pd
import numpy as np

def check_na(dataset):
    # Here we will check the percentage of nan values present in each feature
    ## 1 -step make the list of features which has missing values
    features_with_na=[features for features in dataset.columns if dataset[features].isnull().sum()>1]
    ## 2- step print the feature name and the percentage of missing values

    for feature in features_with_na:
        return print(feature, np.round(dataset[feature].isnull().mean(), 4),  ' % missing values')
    #return pycaret.internal.tabular.check_na(dataset=dataset)