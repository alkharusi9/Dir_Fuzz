#!/usr/bin/python

import requests
import time
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

target = input(bcolors.WARNING+"Enter the target's domain name:"+bcolors.ENDC)

choice = input(''' 
    1) Find hidden directories
    2) XSS vulnerbality 
    3) Click-jacking attack
    Choose one of the above: ''')


def banner():
    print(bcolors.FAIL + """%s     
                         
                         
             &&       %%                                &&       %%                   &&%            &&
             &&      %%                                 &&      %%                    &&%%           &&
             &&     %%                                  &&     %%                     && %%          && 
             &&    %%                                   &&    %%                      &&  %%         &&
             &&   %%                                    &&   %%                       &&   %%        &&
             &&  %%                                     &&  %%                        &&    %%       &&
             && %%                                      && %%                         &&     %%      &&
             &&%%%                                      &&%%                          &&      %%     &&
             && %%                                      &&%%          &&&&&&&&&&      &&       %%    &&
             &&  %%           %% %%%%%    %%%%%%%%%%    && %%        &&         &&    &&        %%   &&
             &&    %%         %%%       %%      %%     &&  %%       &&         &&    &&         %%  &&
             &&     %%        %%         %%      %%     &&   %%      &&&&&&&&&&&&     &&          %% &&
             &&       %%      %%         %%      %%     &&    %%     &&               &&           %%&&
             &&        %%     %%         %%      %%     &&     %%    &&               &&            %&&
             &&         %%    %%         %%%%%%%%%%%%   &&      %%    %&&&&&&&&&      &&             %&
                                                     %%
                        |%s%s                                                          
                        # Coded By Alsalt Alkharosi - @0x_pwner
            """ + bcolors.ENDC)


def Scanner():
    global target

    file_name = input(bcolors.WARNING+"Enter the wordlist's name:"+bcolors.ENDC)
    wordlist = open(file_name,'r')
    output = open('targets.vcs','w')

    print(bcolors.OKBLUE + '[!] Please wait, looking for valid directories....' + bcolors.ENDC)
    time.sleep(1)
    print(bcolors.OKBLUE + '[!] The tool is still scanning.....' + bcolors.ENDC)
    time.sleep(2)
    for x in wordlist.readlines():
        try:
            directory = x.strip('\n')
            url = target+'/'+directory
            r = requests.get(url)
            if r.status_code==200:
                print(bcolors.OKGREEN+'[+]'+url+'\n'+bcolors.ENDC)
                output.write(bcolors.OKGREEN + '[+]'+url+ bcolors.ENDC)

            else:
                print(bcolors.FAIL+'[-]'+url+bcolors.ENDC)
        except Exception as e:
                print(e)

        except KeyboardInterrupt:
                print(bcolors.WARNING+'[!] You clicked CTRL+C to stop the scan!'+bcolors.ENDC)
                break

def XSS_vulnerbality():
    global target
    try:
        r = requests.get(target)
        print(bcolors.WARNING+'[*] Now Scanning....'+bcolors.ENDC)
        time.sleep(2)
        if 'X-XSS-Protection' in r.headers:
            print(bcolors.OKGREEN+'[!]'+target,'is not vulnerable to XSS attack, however you may try few payloads!'+bcolors.ENDC)
        else:
            print(bcolors.FAIL+'[!]'+target,'is vulnerable to XSS attack'+bcolors.ENDC)
    except KeyboardInterrupt:
        print(bcolors.FAIL+'[!] You clicked CTRL+C to stop the scan!'+bcolors.ENDC)
    except:
        print(bcolors.FAIL+"[!] Something went wrong!"+bcolors.ENDC)


def clickJacking():
    global target
    try:
        r = requests.get(target)
        headers = r.headers
        print(bcolors.WARNING + '[*] Now scanning..' + bcolors.ENDC)
        time.sleep(2)
        if 'X-Frame-Options' in headers:
            print(bcolors.OKGREEN+"[!] "+target+' is not vulnerable to click-jacking attack!'+bcolors.ENDC)
        else:
            print(bcolors.FAIL+'[!]'+target+' is vulnerable to click-jacking attack!'+bcolors.ENDC)

    except KeyboardInterrupt:
        print(bcolors.FAIL+'[!] You clicked CTRL+C'+bcolors.ENDC)
    except:
        print(bcolors.FAIL+'[!] Something went wrong!')


def main():
    global choice
    
    banner()

    if choice == '1':
        return Scanner()
    elif choice == '2':
        return XSS_vulnerbality()
    elif choice == '3':
        return clickJacking()

if __name__=='__main__':
    main()



