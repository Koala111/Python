import os

def pre_search_file(location,filename):
    #精确查找文件
    search_files=[]
    for root,dirs,files in os.walk(location):
        for file in files:
            #拼接文件完整路径
            path=os.path.join(root,file)
            path=os.path.normcase(path)
            #文件名相同
            if file==filename:
                search_files.append(path)
    return search_files
    
    
def blur_search_file(location,substring):
    #模糊查找文件
    search_files=[]
    for root,dirs,files in os.walk(location):
        for file in files:
            #拼接文件完整路径
            path=os.path.join(root,file)
            path=os.path.normcase(path)
            #文件名相同
            if substring in file:
                search_files.append(path)
    return search_files
    
def search_file_type(location,file_suffix):
    #查找特定文件类型
    search_files=[]
    for root,dirs,files in os.walk(location):
        for file in files:
            #拼接文件完整路径
            path=os.path.join(root,file)
            path=os.path.normcase(path)
            #文件名相同
            if file.endswith(file_suffix):
                search_files.append(path)
    return search_files
    
if __name__=="__main__":
    while True:
        print("****************************")
        print('1:精确查找文件')
        print('2:模糊查找文件')
        print('3:查找特定文件')
        select=int(input('请选择：'))
        if select==1:
            filename=input("请输入文件名称：")
            #查找当前目录
            result=pre_search_file('.',filename)
        if select==2:
            substring=input("请输入文件子串：")
            #查找D目录
            result=blur_search_file('.',substring)
        if select==3:
            type=input("请输入文件后缀名：")
            #查找指定目录
            result=search_file_type('F://',type)
        for item in result:
            print(item)
        
        