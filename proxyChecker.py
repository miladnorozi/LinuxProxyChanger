import urllib2
import os, time, requests, sys, threading


def checkProxy(Proxy):
    try:
        url ="https://google.com"
        sess = requests.session()
        sess.proxies = {'http':Proxy}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                          ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        result = sess.get(url, timeout=5, proxies={'http': Proxy})
        if result.status_code == 200:
            print "1"
        else:
            print "0"
    except:
        print ('something is wrong in checkProxy method')

proxy = sys.argv[1]
checkProxy(proxy)
