import os
import shutil

if not os.path.exists('F:\\demo'):
	os.mkdir('F:\\demo')
#文件夹后面加上/#把c编程的所有不是以.c结尾的文件都删除掉，减少磁盘文件内存
path = 'F:\\demo'

for dirpath,dirnames,filenames in os.walk(path):
	for filename in filenames:
		if (filename.endswith('.o')|filename.endswith('.exe')):
			path_file =dirpath +'\\'+ filename
			print(f'发现文件{path_file}')
			#print(os.listdir(os.getcwd()))
			os.remove(path_file)
			print(f'删除文件{filename}成功')
			