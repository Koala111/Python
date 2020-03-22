import urllib.request  
from bs4 import BeautifulSoup
url = urllib.request.urlopen("http://www.primalsecurity.net") #用urlopen必须用request,python3要求 
output = BeautifulSoup(url.read(), 'lxml')
output.title

