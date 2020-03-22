from lib import data_excel, telnet_main
import time

class main():
    def __init__(self):
        self.host_ip='192.168.1.1'
        self.username='root'       #telnet账户
        self.password='hg2x0'    #telnet密码
        self.flag = 0
        self.crosswise = 0
        self.vertical = 0
        self.telnet_operation = telnet_main.TelnetClient()
        self.dataExcel = data_excel.DataWtExcel()
        self.dataExcel.run_data_excel(0, 0, '内存')
        self.dataExcel.run_data_excel(0, 1, 'CPU')

    def run(self):
        if self.telnet_operation.login_host(self.host_ip, self.username, self.password):

            free = str(self.telnet_operation.import_content('free')).split()
            print(free)     #打印输入free命令后，所有的字符
            print(free[9])  #打印第17个字符，以确定17个字符是否为空闲内存

            cpu = str(self.telnet_operation.import_content('top -n 1')).split()
            print(cpu)      #打印输入top命令后，所有的字符
            print(cpu[21])  #打印第21个字符，以确定21个字符是否为空闲cpu

            self.flag = self.flag + 1
            self.crosswise = self.crosswise + 1

            if int(self.flag) <= 65536:
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, free[9])  #使用第10个字符记录到xls文件，内存条目中,free前面的，
                self.dataExcel.run_data_excel(self.crosswise, self.vertical+1, cpu[21]) #使用第22个字符记录到xls文件，cpu条目中，idle前面的
            else:
                self.crosswise = 0
                self.vertical = self.vertical + 2
                self.flag = 0
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, content)

if __name__ == '__main__':
    main = main()
    while True:
        main.run()
        time.sleep(10)
        print('记录成功')