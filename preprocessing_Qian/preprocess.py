import os
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
import cPickle

def cleanVehData(fpath):
    """
    This function takes as input a path to data file, and cleans it to eliminate missing values
    It returns a pandas DataFrame with no missing value
    """
    df = pd.read_csv(fpath, parse_dates=["PurchDate"]).set_index("RefId")
    # Drop PRIMEUNIT and AUCGUART due to large number of missing values, WheelTypeID due to redundancy with WheelType
    df = df.drop(["PRIMEUNIT", "AUCGUART", "WheelTypeID"], axis = 1)
    # drop buyer number which is an index
    df = df.drop("BYRNO", axis=1)
    # drop records with missing values in reference prices, Color, and Trim, which are hard to fill
    df = df.dropna(axis=0, subset=["MMRAcquisitionAuctionAveragePrice", "MMRAcquisitionAuctionCleanPrice", \
                                   "MMRAcquisitionRetailAveragePrice", "MMRAcquisitonRetailCleanPrice", \
                                   "MMRCurrentAuctionAveragePrice", "MMRCurrentAuctionCleanPrice", \
                                   "MMRCurrentRetailAveragePrice", "MMRCurrentRetailCleanPrice", "Color", "Trim"])
    # Fill WheelType with the largest count value from vehicles with the same Model and Trim
    for i in df[df.WheelType.isnull()].index:
        temp = df.WheelType[(df.Model == df.Model[i]) & (df.Trim == df.Trim[i])].value_counts().index
        if len(temp) > 0:
            df.WheelType[i] = temp[0]
    # Drop records with missing values in WheelType that cannot be filled with abovementioned method
    df = df.dropna(axis=0, subset=["WheelType"])
    # Fill all other missing values with the same method described above
    for k in range(df.shape[1]):
        isna = df.iloc[:,k].isnull()
        if isna.any():
            for i in df[isna].index:
                temp = df.iloc[:,k][(df.Model == df.Model[i]) & (df.Trim == df.Trim[i])].value_counts().index
                if len(temp) > 0:
                    df.iloc[:,k][i] = temp[0]
    return df

def addPriceDiff(df):
    """
    This function takes as input a pandas DataFrame, and calculates price differences between the eight
    reference prices in place.
    It does not return anything
    """
    # Create list for columns names that contains the eight reference prices
    names = ["MMRAcquisitionAuctionAveragePrice", "MMRAcquisitionAuctionCleanPrice", \
             "MMRAcquisitionRetailAveragePrice", "MMRAcquisitonRetailCleanPrice", \
             "MMRCurrentAuctionAveragePrice", "MMRCurrentAuctionCleanPrice", \
             "MMRCurrentRetailAveragePrice", "MMRCurrentRetailCleanPrice", "VehBCost"]
    # Create list for abbreviations of the eight column names to be used in creating new features
    abbrs = ['AAAP', 'AACP', 'ARAP', 'ARCP', 'CAAP', 'CACP', 'CRAP', 'CRCP', 'VehBCost']
    # Calculate difference between each other and store in df
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if i != j:
                df[abbrs[i] + '_' + abbrs[j] + '_diff'] = df[names[i]] - df[names[j]]

def transformVar(df):
    """
    This function takes as input a pandas DataFrame and transforms all categorical variables to dummy variables
    It returns a new DataFrame with all categorical variables replaced by dummy variables
    """
    # Drop Model due to too many levels and redundancy with Trim and SubModel
    # Drop VNZIP1 due to too many levels and redundancy with VNST
    df = df.drop(["Model", "VNZIP1"], axis = 1)
    # Use regex to stardardize format for SubModel
    df.SubModel = df.SubModel.replace({r'([A-Za-z0-9]*\s)([A-Za-z0-9\.\-]*)\s([A-Za-z0-9\.\s\-/])*': r'\1\2'}, regex=True)
    # Fix inconsistency in input for Transimission
    df.Transmission = df.Transmission.replace('Manual', 'MANUAL')
    # Transform to dummy variables
    for i in df.columns:
        if df[i].dtype == 'object':
            temp = df[i].value_counts()
            # if the variable has more than 30 class levels, aggregate less frequent levels to OTHER
            if len(temp) > 30:
                df[i] = df[i].replace(to_replace=temp.index[temp < 100], value="OTHER")
            df = pd.concat([df, pd.get_dummies(df[i], prefix=i)], axis=1)
            df = df.drop(i, axis=1)
    return df

def standardizeDF(train_X, test_X, create_helper=False):
    """
    This function takes as input two pandas DataFrames and standardizes all numerical (non-binary non-date) columns
    in place. Date and year are left unstandardized for further analysis
    It also creates helper file for deployment if create_helper is true
    There's no return value
    """
    # Identify columns to standardize
    toStd = train_X.columns[range(2, 13) + range(14, 51)]
    # Calculate means and standard deviations for those columns
    mean = train_X[toStd].mean()
    std = train_X[toStd].std()
    # Create helper file for deployment if create_helper is true
    if create_helper:
        helper = {'mean' : mean, 'std' : std, 'columns' : train_X.columns[2:]}
        dpath = os.path.join(os.pardir, 'Deployment_Qian', 'helper2.pkl')
        output = open(dpath, 'wb')
        cPickle.dump(helper, output)
        output.close()
    # Standardize both train_X and test_X with the same parameters
    train_X[toStd] = (train_X[toStd] - mean) / std
    test_X[toStd] = (test_X[toStd] - mean) / std

def load_data(create_helper=False):
    """
    This function wraps up the above four functions. It reads the dataset, cleans it, does transformation,
    splits it into training and test set, and finally standardize the data.
    It also creates helper file for deployment if create_helper is true
    Change the fpath if data is in another directory
    """
    # The path to data files, assuming it's in the folder "Data" which is in the same directory as
    # the git directory
    path = os.pardir
    fpath = os.path.join(path, os.pardir, "Data", "training.csv")
    # Read and clean the dataset
    dataset = cleanVehData(fpath)
    # create helper file for deployment if create_helper is true
    if create_helper:
        helper = {}
        for i in dataset.TopThreeAmericanName.value_counts().index:
            helper[i] = dataset.Make[dataset.TopThreeAmericanName == i].value_counts().index
        helper['Make_OTHER'] = dataset.Make.value_counts()[dataset.Make.value_counts() < 100].index
        helper['Columns'] = dataset.columns
        dpath = os.path.join(path, 'Deployment_Qian', 'helper.pkl')
        output = open(dpath, 'wb')
        cPickle.dump(helper, output)
        output.close()
    # Add differences between reference prices
    addPriceDiff(dataset)
    # Transform categorical data to dummy variables
    dataset = transformVar(dataset)
    # Split into training and test data
    train_X, test_X, train_y, test_y = train_test_split(dataset.drop("IsBadBuy", axis=1), dataset.IsBadBuy, \
                                                        test_size=0.3, random_state=4531)
    # Transfer back to pandas DataFrame
    train_X = pd.DataFrame(train_X, columns=dataset.columns[1:])
    test_X = pd.DataFrame(test_X, columns=dataset.columns[1:])
    train_y = pd.DataFrame(train_y, columns=['IsBadBuy'])
    test_y = pd.DataFrame(test_y, columns=['IsBadBuy'])
    # Standardize train_X and test_X
    standardizeDF(train_X, test_X, create_helper)
    return train_X, train_y, test_X, test_y
