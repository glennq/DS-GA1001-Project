log
===
#### Record everything here.

2014-11-11
---
To get started with some primary investigation of this classification problem, I am in charge of Decisiontree and Randomforest model. Prior t training, I split the dataset into 5:2:2 as the proportions of training set, validation set and testing set, of course randonly. Training set is clearly used for training, validation set is mainly used for tunning the parameters whereas testing set is where the result eventually comes from. We may use AUC as the measurement.

For Decisiontree model, I adopt Scikit-learn off-the-shell model. In total I trained 400 models which would be equipped by different combinations of 'min_samples_split', 'min_sample_leaf' and 'max_depth'. The best model performed in validation set yields a AUC of 67.9 on testing set.

For Random Forest, I trained 2400 models with different 'min_samples_split', 'min_sample_leaf', 'max_depth' and 'n_estimators'. The best model selected by validation set obtains AUC of 71.7 on testing set.

