import os
import urllib.request as req
from urllib.parse import urlparse
import sys

# takes a list of urls and downloads the files specified at the end of the link
def download(urls):
    for url in urls:
        # using urlparse to get the url in components
        urlstring = urlparse(url)

        # making stringarray of the path from the url
        urlsplit = urlstring.path.split("/")
        
        # to defines the last part of the url, where the file is to be saved
        to = urlsplit[-1]

        # saves the file as intended
        req.urlretrieve(url, to)
        print("Downloading file to ./", to, sep="")

