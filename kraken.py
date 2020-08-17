#!/usr/bin/python3

import requests
import time
import sys
import socket

try:
    import nmap
except ImportError:
    import os
    print("The python-nmap library is not installed, installing now!")
    os.system('pip install python-nmap')
    print('[!] The nmap library has been installed, please restart kraken!')
    quit()
except Exception:
    print('It seems the nmap library was not installed, please try intsalling it manually')     
    quit()

    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
    print(bcolors.FAIL + """%s     


             &&       %%                                &&       %%                               
             &&      %%                                 &&      %%                    &%%           &&
             &&     %%                                  &&     %%                     &&%%          && 
             &&    %%                                   &&    %%                      && %%         &&
             &&   %%                                    &&   %%                       &&  %%        &&
             &&  %%                                     &&  %%                        &&   %%       &&
             && %%                                      && %%                         &&    %%      &&
             &&%%%                                      &&%%                          &&     %%     &&
             && %%                                  %   &&%%          &&&&&&&&&&      &&      %%    &&
             &&  %%           %% %%%%%    %%%%%%%%%%    && %%        &&         &&    &&       %%   &&
             &&    %%         %%%       %%        %%    &&  %%       &&         &&    &&        %%  &&
             &&     %%        %%        %%        %%    &&   %%      &&&&&&&&&&&&     &&         %% &&
             &&       %%      %%        %%        %%    &&    %%     &&               &&          %%&&
             &&        %%     %%        %%        %%    &&     %%    &&               &&           %&&
             &&         %%    %%         %%%%%%%%%%%%   &&      %%    %&&&&&&&&&      &&            %&
                                                     %%
                        |%s%s                                                          
                        # Coded By Alsalt Alkharosi - @0x_pwner
            """ + bcolors.ENDC)


target = input(bcolors.WARNING + "Enter the target's domain name(Please don't include 'https://'):" + bcolors.ENDC)
ip_add = socket.gethostbyname(target)
print('The IP Address for the target is:',ip_add)
choice = input(''' 
    1) nmap Scan  
    2) Find hidden directories
    3) Find subdomians
    4) XSS vulnerbality 
    5) Click-jacking attack
    Choose one of the above: ''')


# Please refer to nmap tool for all features and functionalities.
# Big thanks go to HackerSploit, this small nmap script was inspired by his original script.
def nScanner():
    global ip_add
    Scanner = nmap.PortScanner()

    Option = input('''\n
    1) Fast Scan
    2) UDP scan 
    3) Super Scan 
    4) Comprehensive scan
    Please choose the type of scan you want to run:''')

    try:
        if Option == '1':
            print('Nmap version:', Scanner.nmap_version())
            Scanner.scan(ip_add, '1-1024', '-v -sS')
            print('IP Status:', Scanner[ip_add].state())
            print(Scanner[ip_add].all_protocols())
            print('Open ports:', Scanner[ip_add]['tcp'].keys())
            print('Details:', Scanner.csv())
        elif Option == '2':
            print('Nmap version:', Scanner.nmap_version())
            Scanner.scan(target, '1-1024', '-v -sU')
            print('IP Status:', Scanner[ip_add].state())
            print('Open ports:', Scanner[ip_add]['udp'].keys())
            print('Details:', Scanner.csv())
        elif Option == '3':
            print('Nmap version:', Scanner.nmap_version())
            Scanner.scan(ip_add, '1-1024', '-v -sS -sV -sC -A -O')
            print('IP Status:', Scanner[ip_add].state())
            print(Scanner[ip_add].all_protocols())
            print('Open ports:', Scanner[ip_add]['tcp'].keys())
            print('Details:', Scanner.csv())
        elif Option == '4':
            print('Nmap version:', Scanner.nmap_version())
            Scanner.scan(ip_add, '1-1024', '-v -sC -sV')
            print('IP Status:', Scanner[ip_add].state())
            print(Scanner[ip_add].all_protocols())
            print('Open ports:', Scanner[ip_add]['tcp'].keys())
            print('Details:', Scanner.csv())
        else:
            print('Please choose a valid option')
    except KeyboardInterrupt:
        print('CTRL+C was clicked to stop the scan!')
    except Exception as e:
        print(e)


def dirFuzz():
    global target

    file_name = input(bcolors.WARNING + "Enter the wordlist's name:" + bcolors.ENDC)
    wordlist = open(file_name, 'r')
    output = open('targets.vcs', 'w')

    print(bcolors.OKBLUE + '[!] Please wait, looking for valid directories....' + bcolors.ENDC)
    time.sleep(1)
    print(bcolors.OKBLUE + '[!] Still scanning.....' + bcolors.ENDC)
    time.sleep(2)
    for x in wordlist.readlines():
        try:
            directory = x.strip('\n')
            url = 'https://'+ target + '/' + directory
            r = requests.get(url)
            if r.status_code == 200:
                print(bcolors.OKGREEN + '[+]' + url + '\n' + bcolors.ENDC)
                output.write(bcolors.OKGREEN + '[+]' + url + bcolors.ENDC)

            else:
                print(bcolors.FAIL + '[-]' + url + bcolors.ENDC)
        except Exception as e:
            print(e)

        except KeyboardInterrupt:
            print(bcolors.WARNING + '[!] You clicked CTRL+C to stop the scan!' + bcolors.ENDC)
            break


def sub_finder():
    global target 
    filename = input(bcolors.WARNING+'Enter the filename:'+bcolors.ENDC)
    file = open(filename,'r')
    output = open('subdomains.vcs','w')
    print(bcolors.FAIL+'[*] Scanning for subdomains'+bcolors.ENDC)
    time.sleep(3)
    print(bcolors.FAIL+'[*] This might take few minutes...'+bcolors.ENDC)

    for subdomain in file.readlines():

            directory = subdomain.strip('\n')
            url = 'https://'+directory+'.'+ target
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(bcolors.OKGREEN+'[+]' + url+bcolors.ENDC)
                output.write('[+]'+url+'\n')
                
            
def XSS_vulnerbality():
    global target
    try:
        url = 'https://'+target
        r = requests.get(url)
        print(bcolors.WARNING + '[*] Now Scanning....' + bcolors.ENDC)
        time.sleep(2)
        if 'X-XSS-Protection' in r.headers:
            print(bcolors.OKGREEN + '[!] X-XSS-Protection header exists!' + bcolors.ENDC)
        else:
            print(bcolors.FAIL + '[!] X-XSS-Protection header does not exist!' + bcolors.ENDC)
    except KeyboardInterrupt:
        print(bcolors.FAIL + '[!] You clicked CTRL+C to stop the scan!' + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + e + bcolors.ENDC)


def clickJacking():
    global target
    try:
       
        url = 'https://' + target
        r = requests.get(url)
        headers = r.headers
        print(bcolors.WARNING + '[*] Now scanning..' + bcolors.ENDC)
        time.sleep(2)
        if 'X-Frame-Options' in headers:
            print(bcolors.OKGREEN + "[!] " + url + ' is not vulnerable to click-jacking attack!' + bcolors.ENDC)
        else:
            print(bcolors.FAIL + '[!]' + url + ' is vulnerable to click-jacking attack!' + bcolors.ENDC)

    except KeyboardInterrupt:
        print(bcolors.FAIL + '[!] You clicked CTRL+C' + bcolors.ENDC)
    except:
        print(bcolors.FAIL + '[!] Something went wrong!')


def main():
    global choice

    banner()

    if choice == '1':
        return nScanner()
    elif choice == '2':
        return dirFuzz()

    elif choice == '3':
        return sub_finder()
    elif choice == '4':
        return XSS_vulnerbality()
    elif choice == '5':
        return clickJacking()
    else:
        print(bcolors.FAIL+'[!] Please choose a valid option!'+bcolors.ENDC)

if __name__ == '__main__':
    main()




    
