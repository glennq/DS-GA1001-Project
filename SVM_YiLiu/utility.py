import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split

def load_data(xpath, ypath):

    """
    train_X.csv, train_y.csv are preprocessed datasets from Glenn Qian.
    This function is to load preprocessed datasets and generate validation set.
    
    Args:
    xpath: path for X dataset, e.g. 'train_X.csv', 'test_X.csv'
    ypath: path for y dataset, e.g. 'train_y.csv', 'test_y.csv'
    
    Return:
    data_X, data_y:
    Dataframe X and dataframe y which are suitable for svm modeling in this case    """

    data_X = pd.read_csv(xpath, sep='\t')
    data_y = pd.read_csv(ypath, sep='\t')
    data_X = data_X.drop('PurchDate', axis = 1)
    data_X = data_X.drop('VehYear', axis = 1)
    data_X = data_X.drop('Unnamed: 0', axis = 1)
    data_y = data_y.drop('Unnamed: 0', axis = 1)
    return data_X, data_y

def split_data(data_X, data_y, split_rate):

    """
    This function is to split dataset into training and validation sets.
    split_rate determines test size, range from 0 to 1, e.g. 0.2.
    
    Return:
    train_x, train_y: training datasets
    validation_x, validation_y: validation datasets
    """

    train_x, validation_x, train_y, validation_y = train_test_split(data_X, data_y, test_size=split_rate, random_state=4531)
    validation_y = validation_y.ravel()
    train_y = train_y.ravel()
    return train_x, validation_x, train_y, validation_y

def data_pca(components, train_x, transform_x):
    
    """
    This function is to do PCA for datasets.
    
    Args:
    components: the amount of variance to be explained, range from 0 to 1, e.g. 0.95
    train_x: the dataset used to fit the PCA
    transform_x: the dataset to be transformed by the fitted PCA
    *note: train_x and transform_x could be the same
    
    Return:
    transform_x_pca_df: the dataframe conducted by PCA
    """

    pca = PCA(n_components=components)
    pca.fit(train_x)
    transform_x_pca = pca.transform(transform_x)
    transform_x_pca_df = pd.DataFrame(transform_x_pca)
    return transform_x_pca_df


