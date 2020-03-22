import requests
from bs4 import BeautifulSoup
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
}
def detial_url(url):
	html=requests.get(url,headers=headers)
	soup = BeautifulSoup(html.text,'lxml')
	title=soup.title.text
	company_name=soup.select('.com-name')[0].text
	'''
	#需要重点掌握，破解加密数字
	salary=soup.select('.job_money.cutom_font')[0].text.encode['utf-8']
	salary=salary.replace(b'',b'')
	salary=salary.replace(b'',b'')
	salary=salary.replace(b'',b'')
	salary=salary.replace(b'',b'')
	salary=salary.decode
	print(salary)
	'''
	print(title)
	print(company_name)
	
	
	
def crawl():	
	for i in range(1):#循环获取各个页面的html
		html=requests.get('https://www.shixiseng.com/interns?page={}&keyword=Python'.format(i),headers=headers)
		soup = BeautifulSoup(html.text,'lxml')
		offers=soup.select('.intern-wrap.intern-item')
		for offer in offers:
			url=offer.select('.f-l.intern-detail__job a')[0]['href']
			#print(url)
			detial_url(url)

crawl()