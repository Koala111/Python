#!/usr/bin/python
#ftp.py
#this script is used to make some ftp operations more convenient
#add upload and download operations  20111210 version0.1

'''
常用函数：

用手册查看，以下只是简略，因为没用用到，[待整理]：

login(user='',passwd='', acct='') 登录到FTP 服务器，所有的参数都是可选的
pwd()                    当前工作目录
cwd(path)                把当前工作目录设置为path
dir([path[,...[,cb]])    显示path 目录里的内容，可选的参数cb 是一个回调函数，会被传给retrlines()方法
nlst([path[,...]) 与dir()类似，但返回一个文件名的列表，而不是显示这些文件名
retrlines(cmd [, cb]) 给定FTP 命令（如“RETR filename”），用于下载文本文件。可选的回调函数cb 用于处理文件的每一行
retrbinary(cmd, cb[,bs=8192[, ra]]) 与retrlines()类似，只是这个指令处理二进制文件。回调函数cb 用于处理每一块（块大小默认为8K）下载的数据。
storlines(cmd, f) 给定FTP 命令（如“STOR filename”），以上传文本文件。要给定一个文件对象f
storbinary(cmd, f[,bs=8192]) 与storlines()类似，只是这个指令处理二进制文件。要给定一个文件对象f，上传块大小bs 默认为8Kbs=8192])
rename(old, new) 把远程文件old 改名为new
delete(path) 删除位于path 的远程文件
mkd(directory) 创建远程目录
————————————————
版权声明：本文为CSDN博主「Heaven13483」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Heaven13483/article/details/46622261

'''
 
import sys,os,ftplib,socket
 
CONST_HOST = "192.168.43.86"
CONST_USERNAME = "modi"
CONST_PWD = "123"
CONST_BUFFER_SIZE = 8192
 
COLOR_NONE = "\033[m"
COLOR_GREEN = "\033[01;32m"
COLOR_RED = "\033[01;31m"
COLOR_YELLOW = "\033[01;33m"
 
def connect():
  try:
    ftp = ftplib.FTP(CONST_HOST)
    ftp.login(CONST_USERNAME,CONST_PWD)
    return ftp
  #except socket.error as socket.gaierror:
  except socket.gaierror:
    print("FTP is unavailable,please check the host,username and password!")
    sys.exit(0)
 
def disconnect(ftp):
  ftp.quit()
 
def upload(ftp, filepath):
  f = open(filepath, "rb")
  file_name = os.path.split(filepath)[-1]
  try:
    ftp.storbinary('STOR %s'%file_name, f, CONST_BUFFER_SIZE)
  except ftplib.error_perm:
    return False
  return True
 
def download(ftp, filename):
  f = open(filename,"wb").write
  try:
    ftp.retrbinary("RETR %s"%filename, f, CONST_BUFFER_SIZE)
  except ftplib.error_perm:
    return False
  return True
 
def list(ftp):
  ftp.dir()
 
def find(ftp,filename):
  ftp_f_list = ftp.nlst()
  if filename in ftp_f_list:
    return True
  else:
    return False
 
def help():
  print("help info:")
  print("[./ftp.py l]\t\t\t show the file list of the ftp site ")
  print("[./ftp.py f filenameA filenameB] check if the file is in the ftp site")
  print("[./ftp.py p filenameA filenameB] upload file into ftp site")
  print("[./ftp.py g filenameA filenameB] get file from ftp site")
  print("[./ftp.py h]\t\t\t show help info")
  print("\t\t\t\t other params are invalid")
 
 
def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print("Params needed!")
    sys.exit(0)
 
  ftp = connect()
 
  if args[0] == "p":
    f_list = args[1:]
    for up_file in f_list:
      if not os.path.exists(up_file):
        print(("UPLOAD: %s "+COLOR_RED+"FAILED"+COLOR_NONE+"  :file not exist")%up_file)
        continue
      elif not os.path.isfile(up_file):
        print(("UPLOAD: %s "+COLOR_RED+"FAILED"+COLOR_NONE+"  :%s is not a file")%(up_file,up_file))
        continue
 
      if upload(ftp, up_file):
        print(("UPLOAD: %s "+COLOR_GREEN+"SUCCESS"+COLOR_NONE)%up_file)
      else:
        print(("UPLOAD: %s "+COLOR_RED+"FAILED"+COLOR_NONE)%up_file)
  elif args[0] == "g":
    f_list = args[1:]
    for down_file in f_list:
      if not find(ftp,down_file):
        print(("DOWNLOAD: %s "+COLOR_RED+"FAILED"+COLOR_NONE+"  :%s is not in the ftp site")%(down_file,down_file))
        continue
 
      if download(ftp, down_file):
        print(("DOWNLOAD: %s "+COLOR_GREEN+"SUCCESS"+COLOR_NONE)%down_file)
      else:
        print(("DOWNLOAD: %s "+COLOR_RED+"FAILED"+COLOR_NONE)%down_file)
 
  elif args[0] == "l":
    list(ftp)
  elif args[0] == "f":
    f_list = args[1:]
    for f_file in f_list:
      if find(ftp,f_file):
        print(("SEARCH: %s "+COLOR_GREEN+"EXIST"+COLOR_NONE)%f_file)
      else:
        print(("SEARCH: %s "+COLOR_RED+"NOT EXIST"+COLOR_NONE)%f_file)
 
  elif args[0] == "h":
    help()
  else:
    print("args are invalid!")
    help()
 
  disconnect(ftp)
 
 
 
if __name__ == "__main__":
  main()