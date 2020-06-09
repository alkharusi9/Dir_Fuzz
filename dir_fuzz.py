#!/usr/bin/python

import sys,requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.FAIL+"""%s     
                 _                                   _____________
                | |                                 |  ___________|
                | |                                 |  |           
                | |                                 |  |                                     __________      ___________
                | |                                 |  |__________                          |_______   |    |_________  |
                | |                                 |  |__________|                                /  /              /  /
      __________| |     __                          |  |                                          /  /              /  /
     |   _______| |    |__|     __                  |  |              __        __               /  /              /  /
     |  |       | |     __     |  |_____            |  |             |  |      |  |             /  /              /  /
     |  |       | |    |  |    |   _____|           |  |             |  |      |  |            /  /              /  /
     |  |       | |    |  |    |  |                 |  |             |  |______|  |           /  /              /  /
     |  |_______| |    |  |    |  |     _________   |  |             |            |          /  /              /  /
     |__________|_|    |__|    |__|    |_________|  |__|             |_________   |         /  /______        /  /_______
                                                                               |  |        /__________|      /___________|    
                |%s%s                                                          |__|
                # Coded By Alsalt Alkharosi - @0x_pwner
    """+bcolors.ENDC)

if len(sys.argv)!=3:
    print(bcolors.WARNING+'Usage: dir_fuzz.py <ip-address> <wordlist>'+bcolors.ENDC)

def Scanner():
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
                print(bcolors.OKGREEN+'[+]'+url+':'+'\n'+bcolors.ENDC)
                output.write(bcolors.OKGREEN+'[+]'+url+'\n'+bcolors.ENDC)
            else:
                print(bcolors.FAIL+'[-]'+url+bcolors.ENDC) # You could change this to 'pass' if you think the output is confusing.
        except Exception as e:
                print(e)

        except KeyboardInterrupt:
                print(bcolors.WARNING+'[-] You clicked CTRL+C to kill the process'+bcolors.ENDC)
                break


if __name__=='__main__':
    Scanner()


