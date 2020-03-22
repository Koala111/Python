import requests
from bs4 import BeautifulSoup
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
}

for i in range(1):#循环获取各个页面的html
	html=requests.get('http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i),headers=headers)

	#print(html.text)
	soup = BeautifulSoup(html.text,'lxml')
	#print(soup.title)
	#print(soup.find_all('p'))
	#soup.select('.article-summery') #class
	#soup.select('p #link') #id
	jokes=soup.select('li.article-summary')
	for joke in jokes:
		title=joke.select('.article-title')[0].text
		print(title)