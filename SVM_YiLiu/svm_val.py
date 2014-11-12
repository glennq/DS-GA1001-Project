import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn import svm, linear_model
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold

from utility import load_data
from utility import data_pca

def xValSVM(dataset, label_name, k, cs):
    '''
    Perform k-fold cross validation on SVM, varies C,
    returns a dictionary where key=c,value=[auc-c1, auc-c2, ...auc-ck].
    '''
    cv = KFold(n=dataset.shape[0], shuffle = True, n_folds = k)
    aucs = {}

    for train_index, test_index in cv:
        tr_f = dataset.iloc[train_index]
        va_f = dataset.iloc[test_index]
    
        for i in cs:
            my_svm_2 = svm.SVC(kernel='linear', C=i, class_weight='auto')
            predicted_y = my_svm_2.fit(tr_f.drop(label_name,1),tr_f[label_name]).decision_function(va_f.drop(label_name,1))
            fpr, tpr, tr = roc_curve(va_f[label_name], predicted_y)
            met = auc(fpr, tpr)

            if (aucs.has_key(i)):
                aucs[i].append(met)
                print 'done with', i
            else:
                aucs[i] = [met]
                print 'done with', i
    return aucs

def avg_stderr(aucs, c):
    """
    This function is to calculate average and standard error of AUC for each C.
    
    Args:
    aucs: a dictionary whose key is parameter C and values are AUCs from different sample.
    c: a list of parameter C conducted cross validation.
    """

    avg=[]
    stderr=[]
    for i in c:
        avg.append(np.mean(aucs[i]))
        stderr.append(np.sqrt(np.var(aucs[i])/((len(aucs[i])))))
    return avg, stderr

def plotxValSVM(avg, stderr, c):
    """
    This function is to plot the result of cross validation.
    
    Args:
    c: the list of parameter C trained in cross validation
    avg: the average AUC for each C
    stderr: the standard error of AUC for each C
    """
    max_refer = np.ones(len(avg))*(max(np.array(avg) - np.array(stderr)))
    fig = plt.figure()
    ax2 = fig.add_subplot(111)
    plt.title('SVM Model AUC vs. Hyper-parameter C')
    plt.plot(np.log10(c), np.array(avg), lw=2.0, label='Mean ACU')
    plt.plot(np.log10(c), np.array(avg)+np.array(stderr),'k--+', lw=2.0, label='Mean+StdErr')
    plt.plot(np.log10(c), np.array(avg)-np.array(stderr),'k--', lw=2.0, label='Mean-StdErr')
    plt.plot(np.log10(c), max_refer,'r', lw=2.0)
    plt.legend(loc=4)
    ax2.set_xlabel('Log10(C)')
    ax2.set_ylabel('Test Set AUC')
    plt.show()

def main():
    
    #load datasets
    train_X, train_Y = load_data('train_X.csv', 'train_y.csv')
    train_X_pca = data_pca(0.95, train_X, train_X)
    train = train_X_pca
    train['Y'] = train_Y
    #set a list of hyperparameter C
    c = [10**i for i in range(-9,2)]
    #conduct X cross validation and return AUCs in each sample for each C
    aucs=xValSVM(train, 'Y', 5, c)
    #calculate the average and standard error of AUC for each C
    avg, stderr = avg_stderr(aucs, c)
    #plot the results of cross validation
    plotxValSVM(avg, stderr, c)

if __name__ == '__main__':
    main()

