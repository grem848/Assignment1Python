import os
import urllib.request as req
from urllib.parse import urlparse
import sys


listen = sys.argv[1:]

def download(urls, to=None):
    for url in urls:
        v = urlparse(url)
        stringarr = v.path.split("/")
        to = stringarr[-1]
        req.urlretrieve(url, to)
        print("Downloading file to ./", to)


download(listen)