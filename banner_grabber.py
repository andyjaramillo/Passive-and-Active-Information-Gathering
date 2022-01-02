import json
import socket
import sys
import urllib
import urllib.request
from urllib.request import urlopen
import requests

#import requests

#from requests.api import get

#comman line argument for the banner we want to grab
if len(sys.argv) < 2:
    print("Usage" + sys.argv[0] + "<url>")
#sys.exit[1] means some error occured. Above would mean that more than two arguments, it would fail   
    sys.exit(1)
#a get request
req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

#we want the host name
gethostby = socket.gethostbyname(sys.argv[1])
print("\n The IP address of " + sys.argv[1] + "is" + gethostby + "\n")

#IP Lookup 
#we need to make arequest to an API, which is ipinfo.io
#apis are often used to optimize work
req_two = requests.get("http://ipinfo.io/"+gethostby+"/json")
print(req_two)
resp_ = json.loads(req_two.text)
print("Location: "+resp_['loc'])
print("Region: "+resp_['region'])
print("Country: "+resp_['country'])
print("city: "+resp_['city'])


