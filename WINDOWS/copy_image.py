import os,sys
import time
import random
import log
def modify_file_suffix(location,file_suffix):
    for root,dirs,files in os.walk(location):
        for filename in files:            
            #如果不是jpg格式的文件，修改后缀名
            portion = os.path.splitext(filename)  # 分离文件名与扩展名
            # 如果后缀是jpg
            if not portion[1] == file_suffix:
                # 重新组合文件名和后缀名
                newname = portion[0] + file_suffix
                os.rename(filename, newname)
    return filename

def search_file(location):
    #精确查找文件
    search_files=[]
    count=0
    for root,dirs,files in os.walk(location):
        for filename in files:            
            #拼接文件完整路径
            path=os.path.join(root,filename)
            path=os.path.normcase(path)
            search_files.append(path)
            count=count+1
    return search_files,count

def random_copy_file():    
    location=r"F:\modi\picture"
    modify_file_suffix(location,'.jpg')
    search_files,count=search_file(location)
    #输出随机图片 
    src_url=search_files[random.randint(1, count-1)]
    des_url=r'f:\python_practice\WEB\mysite\polls\static\polls\images\background.jpg'
    # des_url=r'f:\modi\background.jpg'
    cmd='copy /y {0} {1}'.format(src_url,des_url)
    log.logger.debug('执行的命令为：{}'.format(cmd))
    # lineno=sys._getframe().f_lineno  # 当前代码的行数
    # basename=os.path.basename(__file__)  # 当前文件名名称
    # log.write_log('DEBUG','执行的命令为：{}'.format(cmd))
    os.system(cmd)
    # log.write_log('INFO','已经成功将{0}目录下文件，覆盖{1}文件'.format(src_url,des_url))
    log.logger.debug('已经成功将{0}目录下文件，覆盖{1}文件'.format(src_url,des_url))

random_copy_file()