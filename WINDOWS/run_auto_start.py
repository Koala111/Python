import os
import time
'''
os.chdir(r"D:\\Program Files\\Firefox\\")
process1 = 'firefox.exe https://blog.csdn.net/Eastmount'
process2 = 'firefox.exe https://www.csdn.net/'
os.system(process1)
os.system(process2)

#cmd只能打开一个客户端
os.chdir(r"F:\\Program Files (x86)\\Dev-Cpp\\")
process3 = 'devcpp.exe'
#p3=os.system(process3)

time.sleep(10)
os.system(r'taskkill /im firefox.exe /f') #关闭firefox软件

os.chdir(r"D:\\Program Files (x86)\\Notepad++\\")
process4 = 'notepad++.exe'
#os.system(process4)

print("congratulation to you,have a nice day!!!")
'''
os.chdir(r"F:\python_practice\WINDOWS")
cmd='python copy_image.py'
os.system(cmd)

os.chdir(r"D:\\Program Files\\Firefox\\")
cmd = 'firefox.exe http://127.0.0.1:8000/'
os.system(cmd)

os.chdir(r"F:\python_practice\WEB\mysite")
cmd='python manage.py runserver'
os.system(cmd)



