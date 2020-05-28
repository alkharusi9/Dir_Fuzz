#!/usr/bin/python

import sys,requests

target = sys.argv[1]
file_name = sys.argv[2]
wordlist = open(file_name,'r')
output = open('targets.vcs','w')

for x in wordlist.readlines():
    try:
        directory = x.strip('\n')
        url = 'http://'+str(target)+'/'+directory+'/'
        r = requests.get(url)
        if r.status_code==200:
            print('[+]'+url+'\n')
            output.write('[+]'+url+'\n')
        else:
            print('[-]'+url)
    except Exception as e:
        print(e)
