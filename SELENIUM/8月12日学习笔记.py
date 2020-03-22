
# coding: utf-8

# # 时间模块
# - WebDriverWait(driver,timeout,pool_frequency = 0.5,ignored_exceptions = None)
#     - timeout 最长超时时间，默认以秒为单位 
#     - pooll_frequency 休眠时间的间隔时间，默认为0.5秒    
#     - ignored_exception 超时后的异常信息   
# - until(method,message = '')
# - until_not(method,message = '')

# # 定位一组对象
# - find_elements 定位一组对象，场景（批量操作对象，定位一些对象）
# 

# In[ ]:


# 勾选3个文本框
from selenium import webdriver
import os

driver = webdriver.Firefox()

file_path = 'file:///' + os.path.abspath('checkbox.html')

driver.get(file_path)

inputs = driver.find_elements_by_tag_name('input')

for input in inputs:
      if input.get_attribute('type') == 'checkbox':
            input.click()

driver.quit()


# In[ ]:


# coding = utf-8
from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

# 选择所有的type 为 checkbox 的元素并单击勾选
checkboxes = driver.find_elements_by_css_selector('input[type = checkbox]')

for checkbox in checkboxes:
    checkbox.click()


print (len(checkboxes))
checkboxes.pop().click()

driver.quit()


# In[ ]:


# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)

# 点击link1链接，弹出下拉列表
driver.find_element_by_link_text('Link1').click()

menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')
#鼠标移动到子元素上

ActionChains(driver).move_to_element(menu).perform()
time.sleep(5)
driver.quit()


# In[ ]:


#coding = utf-8
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)

driver.implicitly_wait(30)
#先找到iframe1(id = f1)
driver.switch_to_frame("f1")
#再找到其下面的iframe2(id = f2)
driver.switch_to_frame("f2")

#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()


# In[ ]:


#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#键盘事件
from selenium.webdriver.common.keys import keys
#休眠时间
import time

url = 'http://baidu.com'

driver = webdriver.Firefox()
driver.get(url)
#获取前面 的title
title = driver.title
#获取当前的URL
url = driver.current_url
#设置休眠时间
driver.sleep(5)#固定休眠时间

driver.implicitly_wait(30)#智能等待时间
Web

driver.find_element_by_id("kw").clear()

#返回百度输入框的宽高
size = driver.find_element_by_id("kw").size
#返回百度输入框的内容
text = dirver.find_element_by_id("kw").text
#获得元素的属性值
attr = dirver.find_element_by_id("kw").get_attribute('type')
#设置该元素的结果是否可见，返回True或False
result = dirver.fine_element_by_id("kw").is_displayed()
#鼠标事件
context_click(content)#右击
double_click(double_content)#双击
drag_and_drop(source,target)#拖动
move_to_element()#鼠标悬停在一个元素上
click_and_hold()#按下鼠标左键在一个元素上
#键盘事件
send_keys(Keys.BACK_SPACE)#删除键(BackSpace)
send_keys(Keys.Key.SPACE)#空格键(Space)
send_keys(Key.TAB)#制表键(Tab)
send_keys(Keys.ESCAPE)#回退键(ESC)
send_keys(Keys.ENTER)#回车键（Enter）
send_keys(Keys.CONTROL,'a')#全选(Ctrl+A)
send_keys(Keys.CONTROL,'c')#复制(Ctrl+C)
send_keys(Keys.CONTROL,'x')#复制(Ctrl+X)
send_keys(Keys.CONTROL,'v')#复制(Ctrl+V)



driver.find_element_by_id("user_name").send_keys(u"username")
#xpath定位
content = driver.find_element_by_xpath("")
#生成用户的行为，存储在actionchains对象中，通过perform()执行存储的行为
right_perform =ActionChains(driver).context_click(content).perform()

driver.find_element_by_id(" ").submit()

driver.quit()


# # 二次定位
# - div = driver.find_element_by_class_name("tang_content").find_element_by_name("userName")
# 

# # 多窗口处理
# ## 获取当前窗口,获取所有窗口
# - nowhandle = driver.current_window_handle
# - allhandles = driver.window_handles

# # alert/confirm/prompt 处理
# - text 返回alter/confirm/prompt
# - accept 点击确认按钮
# - dimiss 点击取消按钮，如果有的话
# send_keys
# 

# # 设置等待时间
# - sleep() 设置固定休眠时间
# - implicitly_wait() webdriver提供的一个超时等待
# - WebDriverWait() 每隔一段时间就会检测当前页面是否存在

# In[1]:


from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#webdriver的使用
element = WebDriverWait(driver,10).until(lambda driver:
                                         driver.find_element_by_id("kw"))
driver.find_element_by_id("kw")
element.send_keys("selenium")

#添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()

#添加固定休眠时间

time.sleep(5)
driver.quit()


# In[ ]:


# 获得当前窗口 nowhandle = driver.current_window_handle
# 获得所有窗口 allhandles = driver.window_handles
# 返回所有窗口的句柄到当前会话 swi


# # alter/confirm/prompt处理
# - switch_to.alter() 定位
# - text 返回中文信息
# - accept 点击确认按钮
# - dismiss 点击取消按钮
# - send_keys 输入信息

# # 下拉框处理
# - file_path = 'file:///'+os.path.abspath('drop_down.html')
# - move_to_element() 鼠标移上去直接弹出

# # 分页处理
# - pages = driver.find_element_by_tag_name("select").find_elements_by_tag_name("option")

# # 上传文件
# - 定位上传按钮，添加本地文件
# - driver.find_element_by_name("file").send_keys("url")

# # 下载文件
# - curl 是利用URL语法在命令行方式下工作的开源文件传输工具
# - browser.download.dir 用于指定你所下载文件的目录
# - os.getcwd 返回当前的目录
# - application/octet-stream 为内容的类型

# # 执行JS
# - 在页面上直接执行JS
# - 在某个已经定位的元素上执行JS
# ## 常用方法
# - execute_script(script,*args) 在当前窗口、框架同步执行javaScript
# - script: javascript 的执行
# - *arg: 适用于任何JavaScript

# # 控制滚动条
# - 注册时法律条文的阅读
# - 操作页面没有在视觉范围，无法进行操作，需要拖动滚动条
# - js = "var q = document.documentElement.ScrollTop = 10000"
# - driver.execute_script(js)

# # cookie处理
# - get_cookies() 获得所有的cookie 信息
# - get_cookie(name) 返回特定的name 有cookie 信息
# - add_cookie(cookie_dict) 添加cookie ,必须有name和value 值 
# - delete_cookie(name) 删除特定的cookie信息
# - delete_all_cookies() 删除所有的cookie信息

# In[ ]:


# 获取对象的属性
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('data-node') == '**********':
        input.click()


# # 验证码问题
# - 去掉验证码
# - 设置万能验证码
# - 验证码识别技术 通过Python-tesseract来识别图片验证码
# - 记录cookie 通过向浏览器中添加cookie 可以绕过登录的验证码 add_cookie()
# - driver.add_cookie('name':'Login_UserNumber','value':'username')

# # webdriver原理
# - WebDriver启动目标浏览器，并绑定到指定端口。作为webdriver的remote server
# - Client端通过CommandExcuter 发送HttPRequest 给remote server 的侦听端口
# - remote server 需要依赖原生的浏览器组件

# 
# 
