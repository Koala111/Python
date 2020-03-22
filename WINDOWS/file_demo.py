import os
from temfile import TemporaryFile #运行完会删除
from temfile import TemporaryDirectory #爬虫用
#r表示读，
#w表示写入，如果没有，会自动创建 
#a表示追加

import os
import time
import datetime
import runpy
#import glob
#import fnmatch

os.chdir(r'F:\python_practice\windows') #进入指定的目录
runpy.run_path('auto.py') #运行auto.py文件

'''
print(os.getcwd()) #输出当前文件所在目录
print(os.path.join('modi','dx')) #自动处理路径连接

#下面这个显示好像不正确
for item in os.listdir('F:\\python_practice'):#列出目录下的所有文件，显示一个列表
	print(item,os.path.isdir(item))
	
for file in os.scandir('F:\\python_practice'):#列出目录下的所有文件，显示一个列表
	print(file.name,file.path,file.is_dir())
	print(file.stat()) #文件的属性
	file_mtime = file.stat().st_mtime
	print(datetime.datetime.fromtimestamp(file_mtime))
	print(file.name,time.ctime(file.stat().st_mtime)) #文件的属性,可读形式显示

that_time = datetime.datetime.fromtimestamp(1567764428)
print(that_time)
print(that_time.hour,that_time.minute,that_time.second)	
'''	

'''
path = 'F:\\python_practice'
for dirpath,dirnames,filenames in os.walk(path):
	print(f'发现文件夹{dirpath}')
	#print(f'发现文件夹名{dirnames}')
	print(f'发现文件{filenames}')
	print(filenames.startswith('a'))
	print(filenames.endswith('.py'))
	
print(glob.glob('*.py')) #通配符
print(glob.glob('*.py')，recursive=True) #递归寻找

print(fnmatch.fnmatch('lesson1.py','le*1.py')) #是否符合这个规则
'''
'''
with open('demo.py','r',encoding='utf-8') as f:
	text=f.readlines()
	print(text)
	
with open('demo.py','a',encoding='utf-8') as f:
	text= 'modi\ndaixiong\n'
	f.write(text)
'''
with TemporaryFile('w+') as f:  #程序运行完毕就结束
	f.write('hello world')
	f.seek(0)
	data = f.readlines() #从光标位置开始读
	print(data)
	
with TemporaryDirectory() as tmp_folder:
	print(f'临时文件夹已经创建：{tmp_folder}')
	
if not os.path.exists('F:\\demo'):
	os.mkdir('F:\\demo')
	#os.mkdirs('F:\\demo\\demo\\demo')

#copy
shutil.copy('file1.txt','./demo')
shutil.copy('file1.txt','./demo.txt') #重新命名
shutil.copytree('原文件夹','新文件夹')	

#move
shutil.move()

#rename
os.rename()
#del
os.remove('file.txt')
shutil.rmtree('')