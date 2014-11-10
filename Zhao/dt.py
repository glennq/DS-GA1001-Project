#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np
from sklearn import tree
from sklearn.grid_search import ParameterGrid
from sklearn.metrics import roc_curve, auc
from dpark import DparkContext
import pickle


def load_data():
    train_x = np.loadtxt('../data/train_x.csv', delimiter=',')
    train_y = np.loadtxt('../data/train_y.csv', delimiter=',')
    test_x = np.loadtxt('../data/test_x.csv', delimiter=',')
    test_y = np.loadtxt('../data/test_y.csv', delimiter=',')
    # Generate validation set
    idx = np.random.permutation(train_x.shape[0])
    tr_sz = len(idx) * 5 // 7 
    train_x_split, train_y_split = train_x[idx[:tr_sz], :], \
                                   train_y[idx[:tr_sz]]
    val_x, val_y = train_x[idx[tr_sz: ], :], train_y[idx[tr_sz:]]
    return train_x_split, train_y_split, val_x, val_y, test_x, test_y


def grid_generator(param_grid):
    grid = list(ParameterGrid(param_grid))
    return grid


def dt_model():
    tr_x, tr_y, va_x, va_y, te_x, te_y = load_data()
    param_grid = {'min_samples_split': range(1, 10000, 1000),
                  'min_samples_leaf': range(1, 10000, 1000),
                 # 'max_leaf_nodes': [0, 100, 1000, 10000],
                  'max_depth': [None, 100, 1000, 10000]}
    param_grid = grid_generator(param_grid)

    # Dpark
    dpark_ctx = DparkContext()

    def map_iter(param):
        idx = param[0][0] * 2 + param[0][1]
        param = param[1]
        m = tree.DecisionTreeClassifier(criterion='entropy', **param)
        print '%d, Start traininig Decision Tree model.' % idx
        m = m.fit(tr_x, tr_y)
        print '%d, Training done.' % idx
        proba = m.predict_proba(va_x)
        fpr, tpr, thresh = roc_curve(va_y, proba[:, 1])
        auc_ = auc(fpr, tpr)
        print '%d, AUC is %f' % (idx, auc_)
        return idx, param, auc_

    print 'It will train %d models' % len(param_grid)
    result_record = dpark_ctx.makeRDD(
                            param_grid, 50
                            ).enumerate(
                            ).map(
                            map_iter
                            ).collect()
    
    file_record = open('result.pkl', 'w')
    pickle.dump(result_record, file_record)
    file_record.close()
    
    # testing
    opt = reduce(lambda x, y: x if x[2] > y[2] else y, result_record)
    m_te = tree.DecisionTreeClassifier(criterion='entropy', **opt[1])
    m = m.fit(tr_x, tr_y)
    proba = m.predict_proba(te_x)
    fpr, tpr, thresh = roc_curve(te_y, proba[:, 1])
    auc_ = auc(fpr, tpr)
    print 'Testing AUC is %f' % auc_


def main():
    dt_model()


if __name__ == '__main__':
    main()
