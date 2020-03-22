from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery
import time
#只实现爬取一页的信息
KEYWORD='iPad'
browser = webdriver.Firefox()
wait=WebDriverWait(browser,10)

def crawl_page(page):
    try:
        url='https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url) 
        time.sleep(10)  #方便人为登录操作
        if page>1:
            page_box=wait.until(
                EC.presence_of_element_located(
            By.CSS_SELECTOR,'input.input.J_Input'))
            
            submit_button.until(
                EC.element_to_be_clickable(
            (By.CSS_SELECTOR,'span.btn.J_Submit')))
            
            page_box.clear()
            page_box.send_keys(page)
            submit_button.click()

        wait.until(
            EC.presence_of_element_located(
            (By.CSS_SELECTOR,'.m-itemlist .items .item')))
        
        get_products()
    except:
        crawl_page(1)

def get_products():
    html=browser.page_source
    doc=PyQuery(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'image':item.find('.img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text(),   
        }
        print(product)
        

crawl_page(1)

