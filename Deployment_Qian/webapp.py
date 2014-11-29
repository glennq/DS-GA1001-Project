from flask import Flask, request, render_template, flash
from sklearn.externals import joblib
from sklearn import linear_model
from olform import *
from functions import *
import cPickle
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inputData():
    form = ReportForm(request.form)
    if request.method == 'POST' and form.validate():
        # read helper data which are in two dictionaries
        pk_file = open('helper.pkl', 'rb')
        helper = cPickle.load(pk_file)
        pk_file.close()
        pk_file2 = open('helper2.pkl', 'rb')
        helper2 = cPickle.load(pk_file2)
        pk_file2.close()
        # read classifier from directory 'model'
        clf = joblib.load(os.path.join('model', 'Lr.pkl')) 
        # create dataframe from form data
        df = pd.DataFrame(form.data, index=[0])
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
        flash(str(prob[:, 1]))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.secret_key = 'why would I tell you my secret k'
    app.run()
