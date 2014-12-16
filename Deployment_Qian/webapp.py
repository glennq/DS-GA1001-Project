from flask import Flask, request, render_template, flash
from sklearn.externals import joblib
from olform import *
from functions import *
import numpy as np
import cPickle
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def inputData():
    """
    This functions gets form data from http request, tranform it to conform
    with preprocessed training data, and applies pre-trained classifier on the
    data, and finally output the result on web page.
    It makes use of Flask and some template files to create the online form
    which accepts input.
    """
    global clf
    form = ReportForm(request.form)
    if request.method == 'POST' and form.validate():
        # read helper data which are in two dictionaries
        pk_file = open('helper.pkl', 'rb')
        helper = cPickle.load(pk_file)
        pk_file.close()
        pk_file2 = open('helper2.pkl', 'rb')
        helper2 = cPickle.load(pk_file2)
        pk_file2.close()
        # create dataframe from form data
        df = pd.DataFrame(form.data, index=[0])
        # convert IsOnlineSale to integer value
        df.IsOnlineSale = int(df.IsOnlineSale)
        # add column TopThreeAmericanName
        TopThree = "OTHER"
        if df.Make[0] in helper["GM"]:
            TopThree = "GM"
        elif df.Make[0] in helper["FORD"]:
            TopThree = "FORD"
        elif df.Make[0] in helper["CHRYSLER"]:
            TopThree = "CHRYSLER"
        df["TopThreeAmericanName"] = TopThree
        # Change Make value to OTHER if in minority
        if df.Make[0] in helper['Make_OTHER']:
            df.Make[0] = 'OTHER'
        # Add price differences
        addPriceDiff(df)
        # transform categorical variables
        df = transformVar(df)
        # reorder columns
        df = df.reindex_axis(helper2['columns'], axis=1)
        df = df.fillna(0, axis=0)
        # standardize data
        standardizeDF(df, helper2['mean'], helper2['std'])
        # predict using classifier
        prob = clf.predict_proba(np.float64(df))
        # output result
        flash('The predicted probability is ' + str(prob[0, 1]))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    # read classifier from directory 'model'
    clf = joblib.load(os.path.join('model', 'rf.pkl'))
    app.secret_key = 'why would I tell you my secret k'
    app.run()
