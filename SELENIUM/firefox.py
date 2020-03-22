from selenium import webdriver
import os

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
search_box = browser.find_element_by_id('kw')
search_box.send_keys('python')
submit_button=browser.find_element_by_id('su')
submit_button.click()
'''


file_path = 'file:///' + os.path.abspath('checkbox.html')


inputs = driver.find_elements_by_tag_name('input')

for input in inputs:
      if input.get_attribute('type') == 'checkbox':
            input.click()

driver.quit()
'''