#-*- coding: utf-8 -*-
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

        # self.username='telnetadmin'           #telnet登录账户
        # self.password='telnetadmin'        #telnet登录密码
        self.username = 'root'  # telnet登录账户
        self.password = 'admin'  # telnet登录密码
        self.su = 'su'  # telnet登录账户
        self.su_pwd = '1234567812345'  # telnet登录密码
        self.flag = 0                   #当前记录次数
        self.crosswise = 0              #excel表格中行
        self.vertical = 0               #excel表格中列
        self.telnet_operation = telnet_main.TelnetClient()
        self.dataExcel = data_excel.DataWtExcel()
        self.dataExcel.run_data_excel(0, 0, 'free_total')
        self.dataExcel.run_data_excel(0, 1, 'free_udevd')

        self.dataExcel.run_data_excel(0, 2, 'free_syslogd')
        self.dataExcel.run_data_excel(0, 3, 'free_klogd')
        self.dataExcel.run_data_excel(0, 4, 'free_wlancfg')
        self.dataExcel.run_data_excel(0, 5, 'free_loop')
        self.dataExcel.run_data_excel(0, 6, 'free_fhoam')
        self.dataExcel.run_data_excel(0, 7, 'free_remd')

        self.dataExcel.run_data_excel(0, 8, 'free_obox_pid')
        self.dataExcel.run_data_excel(0, 9, 'free_server')
        self.dataExcel.run_data_excel(0, 10, 'free_vswitchd')
        self.dataExcel.run_data_excel(0, 11, 'free_ram')
        self.dataExcel.run_data_excel(0, 12, 'free_cm')
        self.dataExcel.run_data_excel(0, 13, 'free_dm')

        self.dataExcel.run_data_excel(0, 14, 'free_inetd')
        self.dataExcel.run_data_excel(0, 15, 'free_rastatus6')
        self.dataExcel.run_data_excel(0, 16, 'free_voip_monitor')
        self.dataExcel.run_data_excel(0, 17, 'free_telnetd')
        self.dataExcel.run_data_excel(0, 18, 'free_udhcpd')
        self.dataExcel.run_data_excel(0, 19, 'free_udhcpc')

        self.dataExcel.run_data_excel(0, 20, 'free_arping')
        self.dataExcel.run_data_excel(0, 21, 'free_pppoe_start')
        self.dataExcel.run_data_excel(0, 22, 'free_pppd')
        self.dataExcel.run_data_excel(0, 23, 'free_hgcsip')

        self.dataExcel.run_data_excel(0, 24, 'free_dnsmasqx')
        self.dataExcel.run_data_excel(0, 25, 'cpu_idle')
    def run(self):
        if self.telnet_operation.login_host(self.host_ip, self.username, self.password, self.su, self.su_pwd):
            #SDN 监控所有进程
            #free_total = str(self.telnet_operation.import_content("free | grep buffers:| awk '{print $4}'")).split()
            free_total = str(self.telnet_operation.import_content("free | grep Mem:| awk '{print $4}'")).split()  #总内存
            # print(free_total)

            free_udevd = str(self.telnet_operation.import_content("cat /proc/`ps | grep udevd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | grep -v grep | awk '{print $2}'")).split()
            # print(free_udevd)
            free_syslogd = str(self.telnet_operation.import_content("cat /proc/`ps | grep syslogd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            # print(free_syslogd)
            free_klogd = str(self.telnet_operation.import_content("cat /proc/`ps | grep logd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_wlancfg   = str(self.telnet_operation.import_content("cat /proc/`ps | grep wlancfg   | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_loop = str(self.telnet_operation.import_content("cat /proc/`ps | grep loop | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_fhoam = str(self.telnet_operation.import_content("cat /proc/`ps | grep fhoam | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_remd = str(self.telnet_operation.import_content("cat /proc/`ps | grep remd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_obox_pid = str(self.telnet_operation.import_content("cat /proc/`ps | grep obox_pid | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_server = str(self.telnet_operation.import_content("cat /proc/`ps | grep ovsdb-server | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_vswitchd = str(self.telnet_operation.import_content("cat /proc/`ps | grep ovs-vswitchd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_ram = str(self.telnet_operation.import_content("cat /proc/`ps | grep ram | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_cm = str(self.telnet_operation.import_content( "cat /proc/`ps | grep cm | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_dm = str(self.telnet_operation.import_content("cat /proc/`ps | grep dm | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_inetd = str(self.telnet_operation.import_content("cat /proc/`ps | grep inetd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_rastatus6 = str(self.telnet_operation.import_content("cat /proc/`ps | grep rastatus | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_voip_monitor = str(self.telnet_operation.import_content("cat /proc/`ps | grep voip_monitor| grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_telnetd = str(self.telnet_operation.import_content( "cat /proc/`ps | grep telnetd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_udhcpd = str(self.telnet_operation.import_content( "cat /proc/`ps | grep udhcpd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_udhcpc = str(self.telnet_operation.import_content("cat /proc/`ps | grep udhcpc | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_arping = str(self.telnet_operation.import_content("cat /proc/`ps | grep arping | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_pppoe_start = str(self.telnet_operation.import_content("cat /proc/`ps | grep pppoe | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_pppd = str(self.telnet_operation.import_content("cat /proc/`ps | grep pppd | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            free_hgcsip = str(self.telnet_operation.import_content("cat /proc/`ps | grep hgcsip | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            print(free_hgcsip)
            free_dnsmasqx = str(self.telnet_operation.import_content("cat /proc/`ps | grep dnsmasqx | grep -vE 'grep' |awk 'NR==1{printf $1}'`/status | grep VmRSS | awk '{printf $2}'")).split()
            print(free_dnsmasqx)
            cpu_idle = str(self.telnet_operation.import_content("top -n 1 | grep CPU: | awk '{print $8 }'")).split()
            print(cpu_idle)

            '''
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            free_gdecms = str(self.telnet_operation.import_content(
                "cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值
            
            free_gdecms = str(self.telnet_operation.import_content("cat /proc/`pidof gdecms`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_gdecms[-2])  # 打印倒数第二个字符即为想要取得的数值

           
            
            free_fhoam = str(self.telnet_operation.import_content(
                "cat /proc/`pidof fhoam`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_fhoam[-2])  # 打印倒数第二个字符即为想要取得的数值

            free_sip = str(self.telnet_operation.import_content(
                "cat /proc/`pidof sip`/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_sip[-2])  # 打印倒数第二个字符即为想要取得的数值

            free_b01odmv3 = str(self.telnet_operation.import_content(
                "cat /proc/4934/status | grep VmSize | grep -v grep | awk '{print $2}'")).split()
            # print(free)     #打印输入命令后，所有的字符
            print(free_b01odmv3[-2])  # 打印倒数第二个字符即为想要取得的数值
            
            
            #cpu_idle = str(self.telnet_operation.import_content("top -n 1 | grep CPU: | awk '{print $8 }'")).split()
            cpu_idle = str(self.telnet_operation.import_content("top -n 1 | grep CPU: | awk '{print $8 }'")).split()
            print(cpu_idle)     #打印输入命令后，所有的字符
            print(cpu_idle[-3])  # 打印倒数第二个字符即为想要取得的数值
'''

            self.flag = self.flag + 1
            self.crosswise = self.crosswise + 1

            if int(self.flag) <= 65536:
                #10G SDN 老版本
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, free_total[-2])

                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 1, free_udevd[-3])  # 记录到xls文件
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 2, free_syslogd[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 3, free_klogd[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 4, free_wlancfg[-1])

                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 5, free_loop[-1])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 6, free_fhoam[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 7, free_remd[-1])  # 记录到xls文件
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 8, free_obox_pid[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 9, free_server[-1])

                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 10, free_vswitchd[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 11, free_ram[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 12, free_cm[-1])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 13, free_dm[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 14, free_inetd[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 15, free_rastatus6[-1])

                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 16, free_voip_monitor[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 17, free_telnetd[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 18, free_udhcpd[-1])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 19, free_udhcpc[-1])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 20, free_arping[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 21, free_pppoe_start[-1])

                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 22, free_pppd[-1])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 23, free_hgcsip[-1])
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 24, free_dnsmasqx[-1])  # 记录到xls文件
                # self.dataExcel.run_data_excel(self.crosswise, self.vertical + 25, cpu_idle[-2])
                '''
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, free_total[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical+1, free_udevd[-3]) #记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 2, free_syslogd[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 3, free_klogd[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 4, free_wlancfg[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 5, free_loop[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 6, free_fhoam[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 7, free_remd[-2])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 8, free_obox_pid[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 9, free_server[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 10, free_vswitchd[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 11, free_ram[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 12, free_cm[-2])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 13, free_dm[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 14, free_inetd[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 15, free_rastatus6[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 16, free_voip_monitor[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 17, free_telnetd[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 18, free_udhcpd[-2])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 19, free_udhcpc[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 20, free_arping[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 21, free_pppoe_start[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 22, free_pppd[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 23, free_hgcsip[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 24, free_dnsmasqx[-2])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 25, cpu_idle[-3])
                '''
                '''
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 2, free_fhoam[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 3, free_sip[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 4, free_b01odmv3[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 5, cpu_idle[-3])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical, free_total[-3])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 1, free_gdecms[-2])  # 记录到xls文件
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 2, free_fhoam[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 3, free_sip[-2])
                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 4, free_b01odmv3[-2])

                self.dataExcel.run_data_excel(self.crosswise, self.vertical + 5, cpu_idle[-3])
''             '''
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
