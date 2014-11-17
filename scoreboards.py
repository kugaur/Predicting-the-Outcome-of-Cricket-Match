import urllib 
from BeautifulSoup import BeautifulSoup
import string

append=list.append
url="http://www.howstat.com.au/cricket/Statistics/Matches/MatchListCountry_ODI.asp?A=IND"
url_contents = urllib.urlopen(url)
page = BeautifulSoup(url_contents.read())
matchlist  = page.findAll(attrs = {'class': "LinkNormal" })
l1=[]
t=1
print 'getting match codes'
for match in matchlist:
    if t%2==0:
        s=match.attrs[1][1].split('=')[1]
        if s not in l1:
            l1.append(s)
    t+=1

print 'saving list as .pkl format'
import cPickle as pickle
f=open("India_url.pkl","wb")
pickle.dump(l1,f,pickle.HIGHEST_PROTOCOL)

f.close()




