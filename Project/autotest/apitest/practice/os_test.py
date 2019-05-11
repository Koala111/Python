from os.path import isdir, isfile

a = 'C:\\Users\\18846\\Desktop\\原型文档\\微信文件下载\\WeChat Files\\qq1462188852\\Files'
b = 'C:\\Users\\18846\\Desktop\\原型文档\\微信文件下载\\WeChat Files\\qq1462188852\\Files\\sql.txt'
print(isfile(a))
print(isfile(a))
print(isdir(a))

# 动态导入模块
try:
    import json
except ImportError:
    import simplejson as json
print(json.dumps({'python':3.6}))

# 调用原来版本的代码
from __future__ import unicode_literals
s = 'am i an unicode?'
print(isinstance(s, unicode))
