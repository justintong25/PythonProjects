import urllib.request
from urllib.request import urlopen

def is_internet():
    try:
        urlopen("http://www.google.com", timeout = 1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False

if is_internet():
    print("Internet is currently working")
else:
    print("Internet is not currently working")