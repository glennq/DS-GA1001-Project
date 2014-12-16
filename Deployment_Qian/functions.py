import pandas as pd


def addPriceDiff(df):
    """
    This function takes as input a pandas DataFrame, and calculates price
    differences between the eight reference prices and the purchasing price
    in place.
    It does not return anything
    """
    # Create list for columns names that contains the eight reference prices
    names = ["MMRAcquisitionAuctionAveragePrice",
             "MMRAcquisitionAuctionCleanPrice",
             "MMRAcquisitionRetailAveragePrice",
             "MMRAcquisitonRetailCleanPrice",
             "MMRCurrentAuctionAveragePrice", "MMRCurrentAuctionCleanPrice",
             "MMRCurrentRetailAveragePrice", "MMRCurrentRetailCleanPrice",
             "VehBCost"]
    # Create list for abbreviations of the eight column names to be used in
    # creating new features
    abbrs = ['AAAP', 'AACP', 'ARAP', 'ARCP', 'CAAP', 'CACP', 'CRAP', 'CRCP',
             'VehBCost']
    # Calculate difference between each other and store in df
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if i != j:
                df[abbrs[i] +
                   '_' + abbrs[j] + '_diff'] = df[names[i]] - df[names[j]]


def transformVar(df):
    """
    This function takes as input a pandas DataFrame and transforms all
    categorical variables to dummy variables.
    It returns a new DataFrame with all categorical variables replaced by
    dummy variables
    """
    # Transform to dummy variables
    for i in df.columns:
        if df[i].dtype == 'object':
            df = pd.concat([df, pd.get_dummies(df[i], prefix=i)], axis=1)
            df = df.drop(i, axis=1)
    return df


def standardizeDF(df, mean, std):
    """
    This function takes as input one pandas DataFrames and the mean and
    standard deviation calculated from training data.
    It then standardizes all numerical (non-binary non-date) columns in place
    according to the given mean and std
    There's no return value
    """
    # Identify columns to standardize
    toStd = df.columns[range(0, 11) + range(12, 49)]
    # Standardize both train_X and test_X with the same parameters
    df[toStd] = (df[toStd] - mean) / std
