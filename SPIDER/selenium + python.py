
# coding: utf-8

# - os.system('D:\\selenium_use_case\\test_case\\%s 1>>log.txt 2>&1'%a)  选取test_case目录下的文件执行，并将执行结果保存到log.txt文件中

# # 引入测试报告与结构优化
# - 测试用例
# - 登录模块
# - 退出模块
# - 用户数据参数化文件
# - 执行所有用例
# - 用例执行结果文件
# 
# # unittest单元测试框架
# - TestSuite() 可以看作一个容器（测试套件）
# - addTest() 可以罗列具体要执行的测试用例 
# - unittest.main() 默认会执行所有以test开头的测试用例
# - makeSuite() 用于生产testsuite对象的实例，把所有的测试用例组装成TestSuite，最后把TestSuite传给TestRunner进行执行
# # time模块
# - time.time() 显示时间戳
# - time.ctime() 显示当前时间的字符串形式
# - time.localtime() 显示当前时间的struct_time形式
# - time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) 格式化输出当前时间
#     - now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
#     - filename = "D:\\"now+'result.html'
#     - fp = file(filename,'wb)
# # init__.py文件解析
# ## 执行import语句步骤
# - 创建一个新的，空的module对象（可能包含多个module)
# - 把这个module对象插入sys.module中
# - 装载module的代码
# - 执行新的module中对应的代码
# - 为了标识一下目录是可引用的包，那么就需要在目录下创建一个__init__.py文件
# - 我们在导入一个包的时候，实际就导入了它的__init__.py文件
# # 用例的读取
# - TestLoader 测试用例加载器，包含多加载测试用例的方法，返回一个测试套件
# - discover(start_dir,pattern = 'test*.py,top_level_dir = None)
#     - start_dir :要测试的模块名或测试用例目录
#     - pattern = 'test*py': 表示用例文件名的匹配原则。星号“*"表示任意多个字符
#     - top_level_dir = None: 测试模块的顶层目录。如果没有顶层目录，默认为None
#     
# 
#     
#     
#     

# # 自动化测试高级应用
# ## 自动发邮件功能
# ### smtp协议的基本命令：
# - HELO 向服务器标识用户身份
# - MAIL 初始化邮件传输
# - RCPT 标识单个的邮件接收人
# - DATA　在单个或多个RCPT 命令后，表示所有的邮件接收人已经标识，并初始化数据传输
# - VRFY 用于验证指定的用户/邮箱是否存在
# - EXPN 验证给定的邮箱列表是否存在
# - HELP 查询服务器支持什么命令
# - NOOP 无操作，服务器应响应OK
# - QUIT 结束会话
# - RSET 重置会话，当前传输被取消
# - MAIL FROM 指定发送者地址
# - RCPT　TO 指明的接收者地址
# ## smtp的两种会话方式
# - 连接163，把信给zzz@163.com
# - 通过自己在sina.com的另一个邮箱来发，先连接sina.com的smtp服务器，然后认证，主要是把要发的163信件，投到sina.com,  sina.com 会把邮件投递到163.com
# # 获取测试报告
# - os.listdir() 用于获取目录下的所有文件列表
# - list.sort() sort()方法用于改变列表中元素的位置，还有一个sorted()内置函数，建立了一种新的迭代排序列表
# - key = lambda fn:
# - lambda 提供了一个运行时动态创建阳光灿烂的日子 的方法
# - os.path.getmtime() 返回文件列表中最新文件的时间
# - os.path.isdir() isdir()判断某一路径是否为目录
# - lists[-1] -1 表示取文件列表的最大值，也就是最新被创建的文件
# - os.path.join() join()方法用来连接字符串，通过路径 与文件名的拼接，我们将得到目录下最新被创建 的文件名的完整路径 
# - sentmail(file_new) 定义一个sentmail()发邮件函数，接收一个参数file_new,表示接收最新生成的测试报告文件
# - open(file_new,'rb') 以读写方式打开最新生成的测试报告文件
# - mail_body = f.read() 读取文件内容，将内容传递给mail_body
# - MIMEText(mail_body._subtype = 'html'._charset = 'utf-8') 文件内容写入到邮件正文，html格式，编码为utf-8
# - sendreport() 用于找最新生成的测试报告文件file_new,调用并将file_new传给sentmail()函数
# # python多进程/线程基础
# - thread.allocate_lock() 返回一个新的锁定对象
# - acquire()/release() 一个原始的锁有两种状态，锁定与解锁，分别对应acquire()和release()方法
# - range() 函数来创建列表包含算术级数
# # threading模块
# - thread不支持守护线程，threading支持守护线程
# - start() 开始线程活动
# - join() 等待线程终止
# 
# 
# 

# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)


# In[2]:


soup = BeautifulSoup(html, features='lxml')
print(soup.h1)


# In[4]:


all_href = soup.find_all('a')
print(all_href)
all_href = [l['href'] for l in all_href]
print('\n', all_href)


# In[5]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)


# In[7]:


soup = BeautifulSoup(html, features='lxml')

# use class to narrow search
month = soup.find_all('li', {"class": "month"})
for m in month:
    print(m.get_text())

jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')              # use jan as a parent
for d in d_jan:
    print(d.get_text())


# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
print(html)


# In[2]:


soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])


# In[4]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]


# In[5]:


url = base_url + his[-1]

html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
print(soup.find('h1').get_text(), '    url: ', his[-1])


# In[8]:


# find valid urls
sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
# print(sub_urls)
if len(sub_urls) != 0:
    his.append(random.sample(sub_urls, 1)[0]['href'])
else:
    # no valid sub link found
    his.pop()
print(his)


# In[9]:


his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()


# In[11]:


import requests
# import webbrowser
param = {"wd": "莫烦Python"}  # 搜索的信息
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
# webbrowser.open(r.url)


# In[14]:


data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
print(r.text)

# Hello there, 莫烦 周!


# In[15]:


file = {'uploadFile': open('./image.png', 'rb')}
r = requests.post(
    'http://pythonscraping.com/files/processing2.php', files=file)
print(r.text)

# The file image.png has been uploaded.


# In[ ]:


payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

# Hey Morvan! Looks like you're still logged into the site!


# In[ ]:





# In[ ]:


session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)

# Hey Morvan! Looks like you're still logged into the site!


# In[ ]:


# 下载文件
import os
os.makedirs('C:/img/', exist_ok=True)

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL, 'C:/img/image1.png')


# In[ ]:


import requests
r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)
r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)


# In[5]:


from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('F:/img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)


# In[4]:


from bs4 import BeautifulSoup
import requests

count = 0
for page in range(1, 12):
    
    URL = "http://www.27270.com/beautiful/oumeitupian/list_47_{}.html".format(page)
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'lxml')
    img_ul = soup.find_all('ul', {"class" : "pic_list"})
    for ul in img_ul:
        imgs = ul.find_all('img')
        for img in imgs:
            url = img['src']
            r = requests.get(url, stream=True)
            # image_name = url.split('/')[-1]
            with open('F:/img/%s.png' % count, 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
            print('Saved %s' % count)
            count += 1


# In[ ]:




