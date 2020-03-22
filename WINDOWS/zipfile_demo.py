import zipfile
import os
path = 'F:\\demo\\常用快捷方式.zip'
os.chdir(r'F:\demo')
'''
with zipfile.ZipFile(path,'r') as zipobj:
	for filename in zipobj.namelist():
		info = zipobj.getinfo(filename)
		new_filename = filename.encode('cp437').decode('gbk')
		print(new_filename,info.file_size,info.compress_size)
		
		
#解压
with zipfile.ZipFile(path,'r') as zipobj:
	for filename in zipobj.namelist():
		correct_path = filename.encode('cp437').decode('gbk')
#		print(zipobj.namelist())
		zipobj.extractall(path='F:\\demo\\解压到这里')
		#zipobj.extractall(path='F:\\demo\\解压到这里',pwd=b'modi')
		#zipobj.extract('notepad测试.txt','F:')
		
#压缩
file_list = ['main.c']
with zipfile.ZipFile('压缩后的文件.zip','w') as zipobj:
	for file in file_list:
		zipobj.write(file)
'''
file_list = ['main1.c']		
with zipfile.ZipFile('压缩后的文件.zip','a') as zipobj: #添加文件进去
	for file in file_list:
		zipobj.write(file)
		
