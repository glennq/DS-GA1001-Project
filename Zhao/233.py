#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division

import os
import pickle
import numpy as np
from sklearn.metrics import roc_curve, auc
from dt import load_data


RF_FILE = 'rf_result.pkl'
DT_FILE = 'dt_result.pkl'


def dt_final():
    from sklearn import tree
    tr_x, tr_y, _, __, te_x, te_y = load_data()
    fl = open(DT_FILE)
    pars = pickle.load(fl)
    fl.close()
    opt = reduce(lambda x, y: x if x[2] > y[2] else y, pars)
    print 'DT best: ', opt[1]
    m = tree.DecisionTreeClassifier(criterion='entropy', **opt[1])
    m = m.fit(tr_x, tr_y)
    proba = m.predict_proba(te_x)
    fpr, tpr, thresh = roc_curve(te_y, proba[:, 1])
    fpr_tpr = np.vstack((fpr, tpr)).T
    np.savetxt('dt_fpr_tpr.csv', fpr_tpr, delimiter=',')


def rf_final():
    from sklearn import ensemble
    tr_x, tr_y, _, __, te_x, te_y = load_data()
    fl = open(RF_FILE)
    pars = pickle.load(fl)
    fl.close()
    opt = reduce(lambda x, y: x if x[2] > y[2] else y, pars)
    print 'RF best: ', opt[1]
    m = ensemble.RandomForestClassifier(criterion='gini', **opt[1])
    m = m.fit(tr_x, tr_y)
    proba = m.predict_proba(te_x)
    fpr, tpr, thresh = roc_curve(te_y, proba[:, 1])
    fpr_tpr = np.vstack((fpr, tpr)).T
    np.savetxt('rf_fpr_tpr.csv', fpr_tpr, delimiter=',')


def main():
    print 'process DT'
    dt_final()
    print 'process RF'
    rf_final()


if __name__ == '__main__':
    main()
