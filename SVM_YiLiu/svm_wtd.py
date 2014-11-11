import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn import svm, linear_model
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split

def load_data():

    """
    train_X.csv, train_y.csv are preprocessed datasets from Glenn Qian.
    This function is to load preprocessed datasets and generate validation set.
    """

    train_X = pd.read_csv('train_X.csv', sep='\t')
    train_y = pd.read_csv('train_y.csv', sep='\t')
    train_X = train_X.drop('PurchDate', axis = 1)
    train_X = train_X.drop('VehYear', axis = 1)
    train_X = train_X.drop('Unnamed: 0', axis = 1)
    train_y = train_y.drop('Unnamed: 0', axis = 1)
    #split trainning set to trainning and validation set 
    train_x, validation_x, train_y, validation_y = train_test_split(train_X, train_y, test_size=0.2, random_state=4531)
    validation_y = validation_y.ravel()
    train_y = train_y.ravel()
    return train_x, validation_x, train_y, validation_y

def data_pca(components, train_x, validation_x):
    """
    This function uses PCA to reduce dimensions of dataset
    """
    pca = PCA(n_components=components)
    pca.fit(train_x)
    train_x_pca = pca.transform(train_x)
    validation_x_pca = pca.transform(validation_x)
    train_x_pca_df = pd.DataFrame(train_x_pca)
    validation_x_pca_df = pd.DataFrame(validation_x_pca)
    return train_x_pca_df, validation_x_pca_df

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
    train_x, validation_x, train_y, validation_y = load_data()
    train_x_pca_df, validation_x_pca_df = data_pca(0.95, train_x, validation_x)
    svm_model(train_x_pca_df,train_y,validation_x_pca_df,validation_y)

if __name__ == '__main__':
    main()



