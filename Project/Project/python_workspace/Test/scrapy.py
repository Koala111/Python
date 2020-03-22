import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.sina.com.cn/'

# 中文乱码问题解决方案
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)