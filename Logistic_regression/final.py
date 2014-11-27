import prepare_data
from prepare_data import *
import prepare_logistic
from prepare_logistic import *
import x_validation
from x_validation import *

def main():
    train_X,train_y,test_X,test_y=prepare_data.main()
    train,train_X,train_y,test_X,test_y=prepare_logistic.main(train_X,train_y,test_X,test_y)
    aucs=x_validation.main(train)

