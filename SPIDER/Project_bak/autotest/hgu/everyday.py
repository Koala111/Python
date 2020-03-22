from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains     # 鼠标事件
driver = webdriver.Firefox()
driver.maximize_window()    # 最大化窗口
# 打开一个网址
driver.get('http://192.168.1.1/cgi-bin/luci')
# 获取焦点
useradmin = driver.find_element_by_xpath("//*[@id='login_username']")
useradmin.send_keys("telecomadmin")
password = driver.find_element_by_xpath("//*[@id='login_password']")
password.send_keys("nE7jA%5m")
submit = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/button")
submit.click()
# time.sleep(10)

# overview = driver.find_element_by_xpath("//*[@id='sub_second_menu_status_status_overview']")
# overview.click()

# inner_frame = driver.find_element_by_xpath('//*[@id="broadband_form"]')  # 移动到中间页面
# # # ActionChains(driver).double_click(double_click).perform()
# # click.click()
# driver.switch_to(inner_frame)




# while True:
#     start = driver.page_source
#     driver.find_element_by_xpath("//*[@id='broadband_form']").send_keys(Keys.Control, Keys.END)
#     time.sleep(1)
#     end = driver.page_source
#     if start == end:
#         break

time.sleep(5)
wan = driver.find_element_by_xpath("//*[@id='sub_second_menu_status_status_wan']")
wan.click()
time.sleep(5)

lan = driver.find_element_by_xpath("//*[@id='sub_second_menu_status_status_lan']")
lan.click()
time.sleep(5)

voice = driver.find_element_by_xpath("//*[@id='sub_second_menu_status_status_voice']")
voice.click()
time.sleep(5)

lan = driver.find_element_by_xpath("//*[@id='sub_second_menu_status_status_remote']")
lan.click()
time.sleep(5)
# driver.implicitly_wait(5000)    # 隐性等待5s，最长

driver.quit()   # 关闭并退出浏览器







# //*[@id="sub_second_menu_status_status_smart"]
# //*[@id="sub_second_menu_status_status_service"]
# //*[@id="sub_second_menu_status_status_interface"]  //*[@id="broadband_form"]





