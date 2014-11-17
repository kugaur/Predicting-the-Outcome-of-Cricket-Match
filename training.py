import csv
import numpy as np

append=list.append

#opening the file raw_data.csv

out=open("training.csv","rb")
raw=csv.reader(out)
#opening file to write training data
out1=open("train_data.csv","wb")
t_data=csv.writer(out1)
t_data.writerow(['Overall Average score','Overall Win percentage','Overall Average score in last 10 matches','Overall Win percentage in last 10 matches','Average score against a particular country','Win percentage against a particular country','Average score by this opposition against India','Average Score against a particular country in last 10 matches','Win percentage against a particular country in last 10 matches','Average score by this opposition against India in last 10 matches','Average score at this venue','Win percentage at this venue','Average score at this venue in last 10 matches','Win percentage at this venue in last 10 matches','Average score at this country venue','Win percentage at this country venue','Average score at this country venue in last 10 matches','Win percentage at this country venue in last 10 matches','Average score batting first/2nd','Win percentage batting 1st/2nd','Average score batting first/2nd in last 10 matches','Win percentage batting 1st/2nd in last 10 matches','Day-Night','Result'])


#creating dictionaries for self,oppose,venue,bat1st/2nd
w_self={'n_match':0,'run':0,'win':0,'run10':[],'win10':[]}
w_oppose={'England':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'Pakistan':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'WestIndies':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'NewZealand':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'Australia':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'Bangladesh':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'SriLanka':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'SouthAfrica':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'Zimbabwe':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]},
          'Kenya':{'n_match':0,'run':0,'win':0,'run_m':0,'run10':[],'win10':[],'run_m10':[]}}

w_venue={}
w_venue_c={}
w_bat={'1st':{'n_match':0,'run':0,'win':0,'run10':[],'win10':[]},'2nd':{'n_match':0,'run':0,'win':0,'run10':[],'win10':[]}}

t=0
X=[]
Y=[]

raw.next()
print 'finding the values'
for row in  raw:
    l=[0 for x in range(0,23)]
    win=0
    if t!=0:
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
            
        l[22]=eval(row[8])
        
        
        if row[9]=='India':
            win=1
        
        t_data.writerow(l)
        
        append(X,l)
        append(Y,win)




    #editing data
        
    #self
    w_self['n_match']+=1
    w_self['run']+=eval(row[4])
    if row[8]=='India':
        w_self['win']+=1
        win=1
    if len(w_self['run10'])<10:
        append(w_self['run10'],eval(row[4]))
        append(w_self['win10'],win)
    else:
        del(w_self['run10'][0])
        del(w_self['win10'][0])
        append(w_self['run10'],eval(row[4]))
        append(w_self['win10'],win)

    #oppose
        
    w_oppose[row[0]]['n_match']+=1
    w_oppose[row[0]]['run']+=eval(row[4])
    w_oppose[row[0]]['win']+=win
    w_oppose[row[0]]['run_m']+=eval(row[5])
    if len(w_oppose[row[0]]['run10'])<10:
        append(w_oppose[row[0]]['run10'],eval(row[4]))
        append(w_oppose[row[0]]['win10'],win)
        append(w_oppose[row[0]]['run_m10'],eval(row[5]))
    else:
        del(w_oppose[row[0]]['run10'][0])
        del(w_oppose[row[0]]['win10'][0])
        del(w_oppose[row[0]]['run_m10'][0])
        append(w_oppose[row[0]]['run10'],eval(row[4]))
        append(w_oppose[row[0]]['win10'],win)
        append(w_oppose[row[0]]['run_m10'],eval(row[5]))


    #venue level2

    if row[1] not in w_venue:
        w_venue[row[1]]={'n_match':1,'run':eval(row[4]),'win':win,'run10':[eval(row[4])],'win10':[win]}
    else:
        w_venue[row[1]]['n_match']+=1
        w_venue[row[1]]['run']+=eval(row[4])
        w_venue[row[1]]['win']+=win
        if len(w_venue[row[1]]['run10'])<10:
            append(w_venue[row[1]]['run10'],eval(row[4]))
            append(w_venue[row[1]]['win10'],win)
        else:
            del(w_venue[row[1]]['run10'][0])
            del(w_venue[row[1]]['win10'][0])
            append(w_venue[row[1]]['run10'],eval(row[4]))
            append(w_venue[row[1]]['win10'],win)
        
    #venue level1
    if row[1] not in w_venue_c:
        w_venue_c[row[2]]={'n_match':1,'run':eval(row[4]),'win':win,'run10':[eval(row[4])],'win10':[win]}
    else:
        w_venue_c[row[2]]['n_match']+=1
        w_venue_c[row[2]]['run']+=eval(row[4])
        w_venue_c[row[2]]['win']+=win
        if len(w_venue_c[row[2]]['run10'])<10:
            append(w_venue_c[row[2]]['run10'],eval(row[4]))
            append(w_venue_c[row[2]]['win10'],win)
        else:
            del(w_venue_c[row[2]]['run10'][0])
            del(w_venue_c[row[2]]['win10'][0])
            append(w_venue_c[row[2]]['run10'],eval(row[4]))
            append(w_venue_c[row[2]]['win10'],win)
        

    #batting 1st or 2nd


    if eval(row[3])==1:
        w_bat['1st']['n_match']+=1
        w_bat['1st']['run']+=eval(row[4])
        w_bat['1st']['win']+=win
        if len(w_bat['1st']['run10'])<10:
            append(w_bat['1st']['run10'],eval(row[4]))
            append(w_bat['1st']['win10'],win)
        else:
            del(w_bat['1st']['run10'][0])
            del(w_bat['1st']['win10'][0])
            append(w_bat['1st']['run10'],eval(row[4]))
            append(w_bat['1st']['win10'],win)
    else:
        w_bat['2nd']['n_match']+=1
        w_bat['2nd']['run']+=eval(row[4])
        w_bat['2nd']['win']+=win
        if len(w_bat['2nd']['run10'])<10:
            append(w_bat['2nd']['run10'],eval(row[4]))
            append(w_bat['2nd']['win10'],win)
        else:
            del(w_bat['2nd']['run10'][0])
            del(w_bat['2nd']['win10'][0])
            append(w_bat['2nd']['run10'],eval(row[4]))
            append(w_bat['2nd']['win10'],win)
    t+=1


out.close()
out1.close()

print 'saving the lists and dictionaries to be used during testing'
import cPickle as pickle
f=open("w_self.pkl","wb")
pickle.dump(w_self,f,pickle.HIGHEST_PROTOCOL)
f.close

f=open("w_oppose.pkl","wb")
pickle.dump(w_oppose,f,pickle.HIGHEST_PROTOCOL)
f.close

f=open("w_venue.pkl","wb")
pickle.dump(w_venue,f,pickle.HIGHEST_PROTOCOL)
f.close

f=open("w_venue_c.pkl","wb")
pickle.dump(w_venue_c,f,pickle.HIGHEST_PROTOCOL)
f.close

f=open("w_bat.pkl","wb")
pickle.dump(w_bat,f,pickle.HIGHEST_PROTOCOL)
f.close

##
##print 'training with linear classifier'
##from sklearn import linear_model
##lm=linear_model.SGDClassifier()
##lm.fit(X,Y)
##print 'saving the model'
##f=open("lm_model.pkl","wb")
##pickle.dump(lm,f,pickle.HIGHEST_PROTOCOL)
##f.close()
##




print 'training with random forest'

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=30,verbose=2,n_jobs=1)
#rf=RandomForestClassifier(n_estimators=50)
rf.fit(X,Y)

print 'saving rf the model'


f=open("rf_model.pkl","wb")
pickle.dump(rf,f,pickle.HIGHEST_PROTOCOL)
f.close()

print 'Training with SVC'
from sklearn.svm import SVC
sv=SVC(kernel='linear')
sv.fit(X,Y)

print 'saving svc model'

f=open("sv_model.pkl","wb")
pickle.dump(sv,f,pickle.HIGHEST_PROTOCOL)
f.close()



print 'done'
