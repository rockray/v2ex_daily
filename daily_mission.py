#! /usr/bin/env python2
__author__ = 'mactavish'

import requests
from bs4 import BeautifulSoup

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

username = ""
password = ""
signin_url = "https://v2ex.com/signin"
mission_url = "http://www.v2ex.com/mission/daily"
host_url = "http://www.v2ex.com"

UA = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
headers = {
    "User-Agent" : UA,
    "Host" : "www.v2ex.com",
    "Referer" : "http://www.v2ex.com/signin",
    "Origin" : "http://www.v2ex.com"
}

session = requests.Session()

signin_page = session.get(signin_url[:4] + signin_url[5:], headers=headers, verify=False)
soup = BeautifulSoup(signin_page.text)
once = soup.find(attrs={'name':'once'})['value']

POST = {
    'u':username,
    'p':password,
    'once':once,
    'next':'/',
}

session.post(signin_url, data=POST, headers=headers, verify=True)
soup = BeautifulSoup(session.get(mission_url, headers=headers, verify=False).text)
credit = soup.find(attrs={'class':'super normal button'})

if credit:
    t = credit['onclick']
    credit_url = host_url + t[t.index('/'):t.rindex("'")]
    print credit_url
    session.get(credit_url, headers=headers, verify=False)
else:
    print "Already clicked today"
