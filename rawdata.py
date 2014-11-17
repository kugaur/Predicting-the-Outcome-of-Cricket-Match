import urllib
from bs4 import BeautifulSoup
import string
import csv
import cPickle as pickle
f=open("India_url.pkl","rb")
l1=pickle.load(f)
f.close()

print 'opening file'
out=open("raw_data1.csv","wb")
output=csv.writer(out)
output.writerow(['Opposition','Venue','Venue Country','Day-Night','Batting 1st/2nd',"India's Score",'Opposition score','wickets taken','wickets given','Result'])

print 'getting data'
count=1
page=[]
for e in l1:
    url="http://www.howstat.com.au/cricket/Statistics/Matches/MatchScorecard_ODI.asp?MatchCode=" + str(e)
    url_contents=urllib.urlopen(url)
    page=BeautifulSoup(url_contents.read())

    #result

    result=page.findAll(attrs={'class':"TextBlack8",'valign':"top"})
    r1=result[2].contents[0].split()
    if r1[0]=='No' or r1[0]=='Match':
        continue

    if r1[0] =='New' or r1[0] =='West' or r1[0]=='East' or r1[0]=='South' or r1[0]=='Sri':
        r=r1[0] +r1[1]
    else:
        r=r1[0]



    #getting day night 
    l_day=result[0].contents[0].split()
    if 'Night' in l_day[4]:
        day=0
    else:
        day=1


    #opposition data  
    opposition = page.findAll(attrs = {'class': "Banner2" })
    l=opposition[0].contents[0]
    l=l.split(',')
    l2=l[0].split()
    l3=l[1].split()
    if len(l)==3:
        l3=l[2].split()
    venue=l3[0]
    
    
    if 'India' not in l2:
        if 'India'==l3[4]:
            if l3[6] =='New' or l3[6]=='West' or l3[6]=='Sri' or l3[6]=='South' or l3[6]=='East':
                oppose=l3[6] + l3[7]
            else:
                oppose=l3[6]
        else:
            if l3[4] =='New' or l3[4]=='West' or l3[4]=='Sri' or l3[4]=='South' or l3[4]=='East':
                oppose=l3[4] + l3[5]
            else:
                oppose=l3[4]
            
    else:
        if 'India' == l2[1]:
            if l2[3] =='New' or l2[3]=='West' or l2[3]=='Sri' or l2[3]=='South' or l2[3]=='East':
                oppose=l2[3] + l2[4]
            else:
                oppose=l2[3]
            
        else:
            if l2[1] =='New' or l2[1]=='West' or l2[1]=='Sri' or l2[1]=='South' or l2[1]=='East':
                oppose=l2[1] + l2[2]
            else:
                oppose=l2[1]
            
    #batting 1st or 2nd
    bat=page.findAll(attrs={'class':"TextBlackBold8",'valign':"top",'colspan':"2"})
    b1=bat[0].contents[0].split()
    b2=bat[1].contents[0].split()
    if b1[0]=='India':
        bat1='1'
    else:
        bat1='0'

    #scores
    score=page.findAll(attrs={'class':"TextBlackBold8",'align':"right" ,'valign':"top"})
    score1=score[5].contents[0].split()[0]
    score2=score[17].contents[0].split()[0]
    if bat1=='1':
        s1=score1
        s2=score2
    else:
        s1=score2
        s2=score1

    #wickets
    wicket=page.findAll(attrs={'class':"TextBlackBold8",'valign':"top"})
    w1=wicket[13].contents[0].split()[0]
    if w1=='All':
        w1='10'
    w2=wicket[31].contents[0].split()[0]
    if w2=='All':
        w2='10'
    if bat1=='0':
        wic1=w1
        wic2=w2
    else:
        wic1=w2
        wic2=w1
       
    output.writerow([oppose,venue,day,bat1,s1,s2,wic1,wic2,r])
    print count
    count+=1
    

out.close()
    
    
    
    
    

    

