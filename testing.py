import csv
import numpy as np
import cPickle as pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

append=list.append

#opening file testing.csv

out=open("testing.csv","rb")
test=csv.reader(out)

print 'getting the dictionaries'


f=open("w_self.pkl","rb")
w_self=pickle.load(f)
f.close()

f=open("w_oppose.pkl","rb")
w_oppose=pickle.load(f)
f.close()

f=open("w_venue.pkl","rb")
w_venue=pickle.load(f)
f.close()

f=open("w_venue_c.pkl","rb")
w_venue_c=pickle.load(f)
f.close()


f=open("w_bat.pkl","rb")
w_bat=pickle.load(f)
f.close()


X=[]
Y=[]


test.next()

for row in test:
    win=0
    l=[0 for x in range(0,23)]
    l[0]=(w_self['run']/float(w_self['n_match']))/205.7
    l[1]=w_self['win']/float(w_self['n_match'])
    l[2]=np.mean(w_self['run10'])/222.0
    l[3]=np.mean(w_self['win10'])
    if w_oppose[row[0]]['n_match']!=0:
        l[4]=(w_oppose[row[0]]['run']/float(w_oppose[row[0]]['n_match']))/206.0
        l[5]=w_oppose[row[0]]['win']/float(w_oppose[row[0]]['n_match'])
        l[6]=(w_oppose[row[0]]['run_m']/float(w_oppose[row[0]]['n_match']))/209.0
        l[7]=np.mean(w_oppose[row[0]]['run10'])/218.0
        l[8]=np.mean(w_oppose[row[0]]['win10'])
        l[9]=np.mean(w_oppose[row[0]]['run_m10'])/220.0

    if row[1] in w_venue:
        l[10]=(w_venue[row[1]]['run']/w_venue[row[1]]['n_match'])/207.0
        l[11]=w_venue[row[1]]['win']/w_venue[row[1]]['n_match']
        l[12]=np.mean(w_venue[row[1]]['run10'])/210.0
        l[13]=np.mean(w_venue[row[1]]['win10'])

    if row[2] in w_venue_c:
        l[14]=(w_venue_c[row[2]]['run']/w_venue_c[row[2]]['n_match'])/221.0
        l[15]=w_venue_c[row[2]]['win']/w_venue_c[row[2]]['n_match']
        l[16]=np.mean(w_venue_c[row[2]]['run10'])/221.0
        l[17]=np.mean(w_venue_c[row[2]]['win10'])
               

    if eval(row[3])==1:
        if w_bat['1st']['n_match']!=0:
            l[18]=(w_bat['1st']['run']/float(w_bat['1st']['n_match']))/205.0
            l[19]=w_bat['1st']['win']/float(w_bat['1st']['n_match'])
            l[20]=np.mean(w_bat['1st']['run10'])/221.0
            l[21]=np.mean(w_bat['1st']['win10'])
    else:
        if w_bat['2nd']['n_match']!=0:
            l[18]=w_bat['2nd']['run']/float(w_bat['2nd']['n_match'])
            l[19]=w_bat['2nd']['win']/float(w_bat['2nd']['n_match'])
            l[20]=np.mean(w_bat['2nd']['run10'])
            l[21]=np.mean(w_bat['2nd']['win10'])
        
    l[22]=eval(row[4])

    
    append(X,l)
    if row[5]=='India':
        win=1
    append(Y,win)


out.close()
##print 'predicting outcome'
##print 'predicting using linear classifier'
from sklearn.metrics import mean_squared_error
##
##f=open("lm_model.pkl","rb")
##model1=pickle.load(f)
##f.close()
##
##y3=model1.predict(X)
##print 'mean square error',mean_squared_error(y3,Y)

print 'prediction using RF model'
f=open("rf_model.pkl","rb")
model2=pickle.load(f)
f.close()

y1=model2.predict(X)

print 'mean square error',mean_squared_error(y1,Y)

print 'prediction using SVC model'
f=open("sv_model.pkl","rb")
model3=pickle.load(f)
f.close()

y2=model3.predict(X)

print 'mean square error',mean_squared_error(y2,Y)







    



