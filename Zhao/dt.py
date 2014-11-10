#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np
from sklearn import tree
from sklearn.grid_search import ParameterGrid
from dpark import DparkContext


def load_data():
    train_x = np.loadtxt('../data/train_x.csv', delimiter=',')
    train_y = np.loadtxt('../data/train_y.csv', delimiter=',')
    test_x = np.loadtxt('../data/test_x.csv', delimiter=',')
    test_y = np.loadtxt('../data/test_y.csv', delimiter=',')
    return train_x, train_y, test_x, test_y


def grid_generator(param_grid):
    grid = list(ParameterGrid(param_grid))
    return grid


def dt_model():
    tr_x, tr_y, te_x, te_y = load_data()
    param_grid = {'min_samples_split': range(1, 10000, 1000),
                  'min_samples_leaf': range(1, 10000, 1000),
                  'max_leaf_nodes': [0, 100, 1000, 10000],
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
        res = m.predict(te_x)
        acc = len(np.where(res == te_y)[0]) / len(te_y)
        print '%d, Accuracy is: %f' % (idx, acc)
        return idx, param, acc

    print 'It will train %d models' % len(param_grid)
    acc_total = dpark_ctx.makeRDD(
                            param_grid, 50
                            ).enumerate(
                            ).map(
                            map_iter
                            ).collect()
    np.savetxt('result.csv', np.array(acc_total), delimiter=',')


def main():
    dt_model()


if __name__ == '__main__':
    main()
