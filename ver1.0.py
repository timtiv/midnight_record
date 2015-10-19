import urllib2
import subprocess, sys
import time
import datetime
from mega import Mega
from bs4 import BeautifulSoup
#Grab HTML by urllib2 and BS
url = urllib2.urlopen('http://hichannel.hinet.net/radio/index.do?id=205').read()
soup = BeautifulSoup(url)

#Find script tab
scripts = soup.find_all('script')
ns = scripts[14]

#Grab var url
mid = ns.text[79:262]
target = mid.replace('\/' , '/')
print target

#Connect to Mega
mega = Mega()
acc = raw_input('User account:')
pwd = raw_input('password:')
m = mega.login(acc,pwd)

#FFmpeg grabing stream
d = datetime.datetime.today()
filename = 'G://record/Midnight_you&me_' + str(d.year) + str(d.month) + str(d.day)
cmd = 'ffmpeg -i '+ target + ' -t 20 -y ' + filename + '.wmv'
retcode = subprocess.call(cmd, shell=False)
if retcode !=0:
    sys.exit(retcode)

#Upload file 
file = m.upload(filename+'.wmv')
m.get_upload_link(file)
print ('Done')