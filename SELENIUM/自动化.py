
# coding: utf-8

# In[ ]:


# 登录模块化
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://passport.kuaibo.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
# 私有云登录用例
    def test_login(self):
        driver = self.driver
        driver = self.driver
        driver.get(self.base_url "")
        driver.maximize_window()
#登录
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("username")
        time.sleep(3)
        #新功能引导
        driver.find_element_by_class_name("guide-ok-btn").click()
        time.sleep(3)
        #退出 
        driver.find_element_by_class_name("Usertool").click()
        time.sleep(2)
        driver.find_element_by_link_text("退出").click()
        time.sleep(2)
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()

        


# In[2]:


def login(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys("username")
    driver.find_element_by_id("dl_an_submit").click()


# In[ ]:


from selenium import webdriver
import os,time
source = open("D:\\abc\\data.txt","r)
values = source.readlines()
source.close()

for serch in values:
    browser = webdriver.Firefox()
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_key(serch)
    browser.find_element_by_id("su").click()
    browser.quit()
    


# source = open("","r")
# un = source.read()
# source.close()
# def login(self):
#     driver = self.driver
#     driver.maximize_window()
#     driver.find_element_by_id("user_name").clear()
#     driver.find_element_by_id("user_name").send_keys(un)
#     time.sleep(3)
#     

# In[ ]:


# coding = utf-8
import userinfo
info = userinfo.zidian()

for un,pw in info.items():
    print un
    print pw


# In[1]:


# Ajax
- 是一种支持动态改变用户界面元素的技术
 try:
     f = file("")
    while True:
        line = freadline()
        if len(line) == 0:
            break
        time.sleep()
        print line
finally:
    f.close()
    print 'Cleaningup ...closed the file'


# filename = raw_input('please input file name')
# if filename == 'hello':
#     raise NameError('input file name error!')
#     #######################
# AssertionError assert语句失败
# AttributeError 试图访问一个对象没有的属性

# In[1]:


from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
try:
    browser.find_element_by_id("kwsss").send_key("selenium")
    browser.find_element_by_id("su").click()
except:
    browser.get_screeshot_as_file("/home/fnngj/python/error_png.png")#截图操作
browser.quit()
    


#  - __init__() 在类的一个对象被建立时，马上运行，可以对你的对象做初始化操作
#  - __  将一个方法声明为private
#  - __init__()方法是一个私有的方法，不能直接被外部使用，为了使用类中的私有成员函数，就可以通过getXX或setXX
#  - __name__ 作为模块的内置属性，就是.py文件的调用方式，两种方式，作为模块被调用和直接 使用，如果__name__ == "__main__"就表示是要直接 执行
#  
