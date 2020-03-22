from lib import data_excel, telnet_main
import time


"""
一，安装相应模块
二，修改main.py文件中，相应参数为自己设备信息
    1，目的ip（默认为：192.168.1.1）
    2，telnet登录账户/密码（默认为：admin/nE7jA%5m）
    3，需要输入的相应命令（默认输入：free/top -n 1）
三，修改telnet_main.py文件中，相应参数为自己设备信息
    1，连接telnet的端口（默认为：23）
    2，telnet登录成功之后，返回值（默认为：#）
"""

class main():
    def __init__(self):
        self.host_ip='192.168.1.1'      #目的主机IP
        self.username='telnetadmin'#电信telnet登录账户
        self.password='nE7jA%5m'  #电信telnet登录密码
        self.su='su'
        self.su_pwd='1234567812345'
        self.flag = 0                   #当前记录次数
        self.crosswise = 0              #excel表格中行
        self.vertical = 0               #excel表格中列
        self.telnet_operation = telnet_main.TelnetClient()
        self.dataExcel = data_excel.DataWtExcel()
        self.dataExcel.run_data_excel(0, 0, '内存')
        self.dataExcel.run_data_excel(0, 1, 'CPU')
        self.dataExcel.run_data_excel(0, 2, 'odmv3')
        # self.dataExcel.run_data_excel(0, 2, 'sip')
        # self.dataExcel.run_data_excel(0, 3, 'dnsmasq')
        # self.dataExcel.run_data_excel(0, 4, 'wifi')
        # self.dataExcel.run_data_excel(0, 5, 'init_scripts_obox')
        # self.dataExcel.run_data_excel(0, 6, 'cm')
        # self.dataExcel.run_data_excel(0, 7, 'dhcpd')
        # self.dataExcel.run_data_excel(0, 8, 'arp')
        # self.dataExcel.run_data_excel(0, 9, 'dhcpc')
        # self.dataExcel.run_data_excel(0, 10, 'pppoe_start')
        # self.dataExcel.run_data_excel(0, 11, 'pppd')

    def run(self):
        if self.telnet_operation.login_host(self.host_ip, self.username, self.password, self.su, self.su_pwd):

            free = str(self.telnet_operation.import_content("free | grep Mem: | awk '{print $4}'")).split()
            print(free)     #打印输入free命令后，所有的字符
            print(free[-2])  # 打印第1个字符，以确定17个字符是否为空闲内存



            cpu = str(self.telnet_operation.import_content("top -n 1 | grep CPU: | awk '{print $8}'")).split()
            print(cpu)      #打印输入top命令后，所有的字符
            print(cpu[10])  # 打印第21个字符，以确定21个字符是否为空闲cpu

            odmv3 = str(self.telnet_operation.import_content("cat /proc/7730/status | grep VmSize | awk '{print $2}'")).split()
            print(odmv3)
            print(odmv3[-2])

            # sip = str(self.telnet_operation.import_content("cat /proc/`pidof hgcsip`/status | grep VmSize |grep -vE 'grep' | awk '{print $2}'")).split()
            # print(sip)
            # print(sip[-3])
            #
            # dnsmasq = str(self.telnet_operation.import_content("cat /proc/`ps | grep dnsmasq |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(dnsmasq)
            # print(dnsmasq[-2])
            #
            # wifi = str(self.telnet_operation.import_content("cat /proc/`ps | grep wlancfg |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(wifi)
            # print(wifi[-2])
            #
            # init_scripts_obox = str(self.telnet_operation.import_content("cat /proc/`ps | grep obox |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(init_scripts_obox)
            # print(init_scripts_obox[-2])
            #
            # cm = str(self.telnet_operation.import_content("cat /proc/`ps | grep sodgw |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(cm)
            # print(cm[-2])
            #
            # dhcpd = str(self.telnet_operation.import_content("cat /proc/`ps | grep dhcpd |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(dhcpd)
            # print(dhcpd[-2])
            #
            # arp = str(self.telnet_operation.import_content("cat /proc/`ps | grep arp | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(arp)
            # print(arp[-2])
            #
            # dhcpc = str(self.telnet_operation.import_content("cat /proc/`ps | grep MNG |grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(dhcpc)
            # print(dhcpc[-2])
            #
            # pppoe_start = str(self.telnet_operation.import_content("cat /proc/`ps | grep pppoe-start |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(pppoe_start)
            # print(pppoe_start[-2])
            #
            # pppd = str(self.telnet_operation.import_content("cat /proc/`ps | grep pppd |grep -vE 'grep' | awk 'NR==1{printf $1}'`/status | grep VmSize | awk '{printf $2}' ")).split()
            # print(pppd)
            # print(pppd[-2])


            self.flag = self.flag + 1
            self.crosswise = self.crosswise + 1

            if int(self.flag) <= 65536:
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, free[-2]) #使用第11个字符记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical+1, cpu[10])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 2, odmv3[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+2, sip[-3])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+3, dnsmasq[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+4, wifi[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+5, init_scripts_obox[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+6, cm[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+7, dhcpd[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+8, arp[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+9, dhcpc[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+10, pppoe_start[-2])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical+11, pppd[-2])


            else:
                self.crosswise = 0
                self.vertical = self.vertical + 2
                self.flag = 0
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, content)
        else:
            print('记录失败')


if __name__ == '__main__':
    main = main()
    flag = 0
    while True:
        main.run()

        flag = flag + 1
        print(flag)
        time.sleep(60)  # 连接一次telnet时间