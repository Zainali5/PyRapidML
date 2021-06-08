
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
    if len(features_with_na) > 0:
        for feature in features_with_na:
            print(feature, np.round(dataset[feature].isnull().mean(), 4),  ' % missing values')
        #return pycaret.internal.tabular.check_na(dataset=dataset)
    else:
        print("No Missing Values")
        
    """
    This function checks missing values and gives the % of missing values in each feature
    

    Example
    -------
    >>> from PyRapidML.eda import check_na
    >>> na_perc = check_na(df)
    
    df: dataframe

         
    """

    
def numerical_features(dataset):
    # list of numerical variables
    numerical_features = [feature for feature in dataset.columns if dataset[feature].dtypes != 'O']

    print('Number of numerical variables: ', len(numerical_features))

    # visualise the numerical variables
    #print(dataset[numerical_features].head())
    ## Numerical variables are usually of 2 type
    ## 1. Continous variable and Discrete Variables

    discrete_feature=[feature for feature in numerical_features if len(dataset[feature].unique())<25] 
    print("Discrete Variables Count: {}".format(len(discrete_feature)))
    
    continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature]
    print("Continuous feature Count {}".format(len(continuous_feature)))
    
    """
    This function tells total numerical features and further tell how many of them are discrete and continuous
    

    Example
    -------
    >>> from PyRapidML.eda import numerical_features
    >>> num_fea = numerical_features(df)
    
    df: dataframe

         
    """
    
