import sklearn.linear_model
from sklearn.linear_model import *
from sklearn.cross_validation import *
from sklearn.metrics import *
import math
from math import *
import matplotlib.pyplot as pl
import numpy as np

#Cross_Validation Function Return dictionary
def xValLR(train, label, k, cs):
    
    aucs = {}
    cv = KFold(n=train.shape[0], n_folds =k)
    for train_index, test_index in cv:
        tr_f = train.iloc[train_index]
        va_f = train.iloc[test_index]
    
        for c in cs:
            Lr = sklearn.linear_model.LogisticRegression(C=c)
            Lr.fit(np.float64(tr_f.drop(label,1)),np.float64(tr_f.y))
            
            met = roc_auc_score(np.float64(va_f.y), Lr.predict_proba(np.float64(va_f.drop(label,1)))[:,1])
        
            if (aucs.has_key(c)):
                aucs[c].append(met)
            else:
                aucs[c] = [met]
        
    return aucs
def plot(aucs,k,cs):
	#Calculate Mean and Std
	meanAUC=[]
	StdErrAUC=[]
	for c in cs:
		meanAUC.append(np.mean(aucs[c]))
		StdErrAUC.append(np.std(aucs[c])/(sqrt(10)))
	#Plot Low, Up, Mean, maxLow
	Low=[]
	Up=[]
	for i in xrange(19):
		Low.append(meanAUC[i]-StdErrAUC[i])
		Up.append(meanAUC[i]+StdErrAUC[i])
	maxLow=np.max(Low)
	cslog=[]
	for c in cs:
		cslog.append(math.log10(c))

	
	pl.plot(cslog, meanAUC, label='meanAUC')
	pl.plot(cslog, Up, 'k--',label='Up')
	pl.plot(cslog, Low, 'k+',label='Low')
	pl.axhline(y=maxLow,color='r',label='maxLow')
	pl.xlabel('Log10(c)')
	pl.title('X-validated AUC by C')
	pl.legend(loc="lower right")
	pl.show()

def main(train):
	k=10
	cs=[1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,10,1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9]
	aucs=xValLR(train,'y', k, cs)
	plot(aucs,k,cs)
	return aucs

