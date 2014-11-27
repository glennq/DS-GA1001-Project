import numpy as np

def main(train_X,train_y,test_X,test_y):

	train=train_X
	train['y']=train_y

	train_X=train_X.drop('PurchDate',1)
	test_X=test_X.drop('PurchDate',1)
	train_X=train_X.drop('VehYear',1)
	test_X=test_X.drop('VehYear',1)

	train=train.drop('PurchDate',1)
	train=train.drop('VehYear',1)


	test_X=np.float64(test_X)
	train_X=np.float64(train_X)
	train_y=np.float64(train_y)
	test_y=np.float64(test_y)

	return train, train_X, train_y, test_X, test_y