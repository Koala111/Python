import telnetlib
import logging
import time
from lib import data_excel
import sys


class TelnetClient():
    def __init__(self):
        self.telnet=telnetlib.Telnet()

    def login_host(self,host_ip,username,password):
        try:
            try:
                self.telnet.close()
                self.telnet.open(host_ip,port=23)   #连接telnet IP和端口

                self.telnet.read_until(b"login:", 10)      #判断连接成功后，返回值为login：就进行下一步输入账户
                self.telnet.write(username.encode('ascii') + b'\n')

                self.telnet.read_until(b"Password:", 10)   #判断输入账户后，返回值为Password:，就进行下一步输入
                self.telnet.write(password.encode('ascii') + b'\n')





                time.sleep(2)
                login_result = self.telnet.read_very_eager().decode('ascii')        #获取输入账号密码后，返回值
                # print(login_result)

                if '#' in login_result:     #判断上一步获取的返回值，是否为#
                    return True
                else:
                    print('账号密码错误')
                    return False
            except:
                return False
        except:
            logging.warning('%s网络连接失败'%host_ip)
            sys.exit(0)

    def import_content(self,content):
        self.telnet.write(content.encode('ascii')+b'\n')
        time.sleep(2)
        content_result=self.telnet.read_very_eager().decode('ascii')
        return content_result



if __name__ == '__main__':
    host_ip='192.168.1.1'
    username='telnetadmin'
    password='nE7jA%5m'
    su='su'
    su_pwd='1234567812345'



    telnet_client=TelnetClient()
    if telnet_client.login_host(host_ip,username,password,su,su_pwd):
        free = str(telnet_client.import_content("top -n 1 | grep CPU: | awk '{print $4}'")).split()[10]
        cpu = str(telnet_client.import_content("top -n 1 | grep CPU: | awk '{print $8}'")).split()[10]

        data_excel = data_excel.DataWtExcel()
        data_excel.run_data_excel(crosswise=4,vertical=7,content=6)





