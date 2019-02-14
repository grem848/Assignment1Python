import webget
import sys

urls = sys.argv[1:]
webget.download(urls)


