import os
import time
import datetime
import runpy
import schedule
#import glob
#import fnmatch
'''
os.chdir(r'F:\python_practice\FH_AUTO_TEST') #进入指定的目录
runpy.run_path('ftp_down.py') #ftp下载镜像到本地
time.sleep(600)
print('镜像成功下载到本地')

runpy.run_path('ftp_down.py') #tftp配置修改成功
print('tftp配置修改成功')

process2 = 'firefox.exe https://www.csdn.net/'
os.system(process1)		      #打开tftp软件
print('打开tftp软件成功')
							  
							  #开始通过tftp传文件到设备中
							  #可以把打包文件一下传进去，之后再解压，就不用一直传了

runpy.run_path('wifi_test.py') #测试wifi功能
time.sleep(600)
print('wifi功能完成')


runpy.run_path('auto.py') #运行auto.py文件
time.sleep(600)
runpy.run_path('auto.py') #运行auto.py文件
time.sleep(600)
runpy.run_path('auto.py') #运行auto.py文件
time.sleep(600)
'''
def job():
	print("我在学习中...")
schedule.every().minutes.do(job)
'''
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10)minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minutes.at(":17")do(job)
'''
while True:
	schedule.run_pending()
	time.sleep(1)
#把所有测试结果放到表格里面
#通过邮件的形式发送出来