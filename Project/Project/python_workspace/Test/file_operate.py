
def wfile():    # 定义写文件函数
    try:
        filename = "D:\\File\\Download\\"+"test.html "   # 定义文件路径和文件名变量  
    except IOError:
        print( "file create error") # 文件异常处理
    else:
        fp = open(filename,'wb')    # 打开写文件
        fp.write("test".encode('utf_8'))
        fp.cose()
    
def rfile():    # define the readalbe function
    try:
        filename = "D:\\File\\Download\\"+"test.html "  # define the readable file path
        fp = open(filename, 'r')    # open the readable file
    except IOError: 
        print("file open error")
    else:
        for f in fp:
            print("file data is" + f)   # print the data
        fp.close()
if __name__ == '__main__':
    wfile()
    rfile()
    print("The operation is done")
