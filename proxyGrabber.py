from bs4 import BeautifulSoup
import urllib2
from pathlib import Path
import os, time, requests, sys, threading


def grabProxies():
    wfile = open('proxies.txt', 'w')
    url = "https://free-proxy-list.net/"
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)
    counter = 0
    soup = BeautifulSoup(con)
    table = soup.find("table")
    for row in table.findAll('tr')[1:10]:
        counter = counter + 1
        col = row.findAll('td')
        col1 = col[0].getText()
        col2 = col[1].getText()
        f = (col1 + ":" + col2)
        checkProxy(str(col1)+":"+str(col2))
    url = "https://www.socks-proxy.net/"

    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)
    counter = 0
    soup = BeautifulSoup(con)
    table = soup.find("table")
    for row in table.findAll('tr')[1:10]:
        counter = counter + 1
        col = row.findAll('td')
        col3 = col[1].getText()
        col2 = col[-8].getText()
        f = (col2 + ":" + col3)
        checkProxy(str(col1)+":"+str(col2))

    url = "https://www.us-proxy.org/"
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)
    counter = 0
    soup = BeautifulSoup(con)
    table = soup.find("table")
    for row in table.findAll('tr')[1:10]:
        counter = counter + 1
        col = row.findAll('td')
        col1 = col[0].getText()
        col2 = col[1].getText()
        checkProxy(str(col1)+":"+str(col2))

def checkProxy(Proxy):
    try:
        url ="https://google.com"
        sess = requests.session()
        sess.proxies = {'http':Proxy}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                          ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        result = sess.get(url, timeout=5, proxies={'http': Proxy})
        if result.status_code == 200:
            with open('okProxy.txt','a') as handler:
                    handler.write(Proxy+'\n')
    except:
        print ('something is wrong in checkProxy method')
grabProxies()
