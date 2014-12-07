Introduction
===========
This is the directory for deployment of our model.

In this directory, we are building an online form with Flask, which takes as input the values for variables necessary for our model, and then output the predicted probability.

To run this thing, you need to follow the next few steps:
1. Run "load\_data(True)" from the folder preprocessing\_Qian, which will create two helper files helper1.pkl and helper2.pkl in Deployment\_Qian
2. Run any model in sklearn, and save the fitted model object with joblib in sklearn.
3. Copy the files created by joblib to Deployment\_Qian/model
4. Run webapp.py directly from this Deployment\_Qian
