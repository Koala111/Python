import os
#无法获得cmd命令的输出
'''
cmd = 'dir'
ping = 'ping www.baidu.com'
os.system(cmd)
os.system('ipconfig')
os.system(ping)

import subprocess

p = subprocess.Popen("ls",
        stdout=subprocess.PIPE, universal_newlines=True)
p.wait()
result_lines = p.stdout.readlines()

for line in result_lines:
    print(line)
'''
#但os.popen可以以字符串形式获得shell下的输出
cmd = r'ping www.baidu.com'
with os.popen(cmd, 'r') as f:
    text = f.read()
str = '丢失 = 0 (0% 丢失)'
if (text.find(str)>=0): #成功返回的是292，失败返回-1
	print('网络通畅，可以执行其它操作！！！')
else:
	print('网络异常，请注意排查问题！！！')
	

'''	
# 输出结果字符串处理
s = text.split("\n")  # 切割换行
result = [x for x in s if x != ''] # 列生成式去掉空
print(result[-3])

'''

	
	
	
	
	
	
	
	
	
	
	