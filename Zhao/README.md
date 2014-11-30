log
===
#### Record everything here.

2014-11-11
---
To get started with some primary investigation of this classification problem, I am in charge of Decisiontree and Randomforest model. Prior t training, I split the dataset into 5:2:2 as the proportions of training set, validation set and testing set, of course randonly. Training set is clearly used for training, validation set is mainly used for tunning the parameters whereas testing set is where the result eventually comes from. We may use AUC as the measurement.

For Decisiontree model, I adopt Scikit-learn off-the-shell model. In total I trained 400 models which would be equipped by different combinations of 'min_samples_split' (from 1 through 10000), 'min_sample_leaf' (from 1 through 10000) and 'max_depth' (from 100 throught 10000). The best model performed in validation set is {'max_depth': 10000, 'min_samples_leaf': 1, 'min_samples_split': 1001} and it yields a AUC of 67.9 on testing set.

For Random Forest, I trained 2400 models with different 'min_samples_split' , 'min_sample_leaf', 'max_depth' and 'n_estimators' (from 10 through 500). The best model selected by validation set is {'max_depth': 1000, 'min_samples_leaf': 1, 'min_samples_split': 1, 'n_estimators': 500} and it obtains AUC of 71.7 on testing set.


2014-11-30
-------
The best parameter for Decision Tree is: {'min_samples_split': 1001, 'max_depth': 10000, 'min_samples_leaf': 1}

The best parameter for Random Forest is: {'min_samples_split': 1, 'n_estimators': 500, 'max_depth': 1000, 'min_samples_leaf': 1}

Corresponded FPR and TPR and saved as .csv file which could be found in this directory. I will finish a short report involving some basic introduction of two models, and the steps how we make them work.

My doc could be seen at: [HERE](https://onedrive.live.com/redir?resid=7E0F473212415A7D!111&authkey=!AKkSv48Eti2tkOA&ithint=file%2cdocx)
