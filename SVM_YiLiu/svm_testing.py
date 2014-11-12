import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc
from sklearn import svm
from sklearn.decomposition import PCA

from utility import load_data
from utility import data_pca

def optimal_svm(optimal_c):
    """
    This function is to calculate AUC for optimal C chose from model selection
    """
    
    #load datasets
    train_X, train_y = load_data('train_X.csv', 'train_y.csv')
    test_X, test_y = load_data('test_X.csv', 'test_y.csv')
    train_X_pca = data_pca(0.95, train_X, train_X)
    test_X_pca = data_pca(0.95, train_X, test_X)
    train_y = np.array(train_y).ravel()
    test_y = np.array(test_y).ravel()
    #set up model with the optimal C
    my_svm = svm.SVC(kernel='linear', C=optimal_c, class_weight='auto')
    predicted_y = my_svm.fit(train_X_pca,train_y).decision_function(test_X_pca)
    fpr, tpr, tr = roc_curve(test_y, predicted_y)
    
    print auc(fpr, tpr)

def main():
    optimal_svm(1e-03)

if __name__ == '__main__':
    main()

