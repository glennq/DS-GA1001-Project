import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn import svm, linear_model
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split

from utility import load_data
from utility import split_data
from utility import data_pca


def svm_model(train_x_pca_df,train_y,validation_x_pca_df,validation_y):

    """
    This function is to build two kinds of svm models with and without setting class weight and compare their performances.
    """

    #Build svm model: uw for unweighted, w for weighted
    my_svm_uw = svm.SVC(C = 0.001, kernel='linear', probability = True)
    my_svm_w = svm.SVC(C = 0.001, kernel='linear', probability = True, class_weight='auto')
    #calculate the predicted probability
    proba_svm_uw = my_svm_uw.fit(train_x_pca_df,train_y).predict_proba(validation_x_pca_df)
    proba_svm_w = my_svm_w.fit(train_x_pca_df,train_y).predict_proba(validation_x_pca_df)
    #calculate AUC
    auc_uw = roc_auc_score(validation_y, proba_svm_uw[:,1])
    auc_w = roc_auc_score(validation_y, proba_svm_w[:,1])
    #prepare to plot ROC curve
    fpr_svm_w, tpr_svm_w, thresholds_svm_w = roc_curve(validation_y, proba_svm_w[:,1])
    fpr_svm_uw, tpr_svm_uw, thresholds_svm_uw = roc_curve(validation_y, proba_svm_uw[:,1])
    #plot ROC curve
    fig = plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    plt.title('ROC Curve for SVM with & without setting class weight')
    plt.plot(fpr_svm_w,tpr_svm_w,'grey', lw = 2.0, label = 'SVM_w ({0:.3f})'.format(auc_w))
    plt.plot(fpr_svm_uw,tpr_svm_uw,'g', lw = 2.0, label = 'SVM_uw ({0:.3f})'.format(auc_uw))
    plt.legend(loc=4)
    plt.show()

def main():
    train_X, train_Y = load_data('train_X.csv', 'train_y.csv')
    train_x, validation_x, train_y, validation_y = split_data(train_X, train_Y, 0.2)
    train_x_pca_df = data_pca(0.95, train_X, train_x)
    validation_x_pca_df = data_pca(0.95, train_X, validation_x)
    svm_model(train_x_pca_df,train_y,validation_x_pca_df,validation_y)

if __name__ == '__main__':
    main()



