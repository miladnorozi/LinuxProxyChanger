__author__ = 'tal89'
from bs4 import BeautifulSoup
import urllib2
import os, time, requests, sys, threading


def GrabProxies():
    wfile = open('proxies.txt', 'w')
    url = " https://free-proxy-list.net/"
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
        wfile.write("\n" + str(col1) + ":" + str(col2))
        print(f)
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
        print(col2 + ":" + col3)
        f = (col2 + ":" + col3)


        wfile.write("\n" + str(col2) + ":" + str(col3))

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
        print(col1 + ":" + col2)
        f = (col1 + ":" + col2)

def checkProxy(Proxy,url):
    try:
            sess = requests.session()
            sess.proxies = {'http':Proxy}
            sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36'
                                            '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            result = sess.get(url, timeout=5, proxies={'http:' Proxy})
            if result.status_code == 200:
                with open('okProxy.txt','a') as xx:
                        xx.write(Proxy+'\n')
