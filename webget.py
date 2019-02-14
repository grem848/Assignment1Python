import os
import urllib.request as req
from urllib.parse import urlparse
import sys

def download(urls):
    for url in urls:
        urlstring = urlparse(url)
        urlsplit = urlstring.path.split("/")
        to = urlsplit[-1]
        req.urlretrieve(url, to)
        print("Downloading file to ./", to, sep="")

