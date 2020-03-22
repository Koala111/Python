# 查找某个目录下的目标文件

import os# 引入操作系统模块
import easygui as g# 引入图形用户界面
result_list= []

def search(filePath,fileName):
    for fileNin in os.listdir(filePath):
        file_dir= os.path.join(filePath, fileN)
    if (os.path.isfile(file_dir))and (fileName in fileN):
        result_list.append(file_dir)
    elif os.path.isdir(file_dir):
        search(file_dir,fileName)
            
def search1(filePath1,fileName):
    for dirPath,dirName,fileNames in os.walk(filePath1):
        for filename in fileNames:
            if fileName in filename:
                result_list.append(os.path.join(dirPath,filename))

        strPath= 'cdefhjkg'  # 默认盘符
strResult=''
path= g.enterbox(msg='请输入文件所在盘符(如:C').rstrip()
path= path.lower()[0]# 截取输入的第一个字符

if path in strPath: #判定输入的第一个字符是否为默认盘符内容
    path= path+ ':\\' # 拼接字符串路径格式如:c:\
    name= g.enterbox(msg='请输入您要查找的文件名').rstrip()

search1(path, name)

if result_list.__len__()> 0: #查询到了
        for path in result_list:

            strResult+= path+'\n'

        g.msgbox(strResult)

else:
    g.msgbox('没有该文件','没有找到')#没有找到

else:
    g.msgbox('请输入正确的盘符')
