import telnetlib
import logging
import time
from lib import data_excel


class TelnetClient():
    def __init__(self):
        self.telnet=telnetlib.Telnet()

    def login_host(self,host_ip,username,password,su,su_pwd):
        try:
            self.telnet.close()
            self.telnet.open(host_ip,port=23)
        except:
            logging.warning('%s网络连接失败'%host_ip)

        self.telnet.read_until(b"login:",10)
        self.telnet.write(username.encode('ascii')+b'\n')

        self.telnet.read_until(b"Password:", 10)
        self.telnet.write(password.encode('ascii') + b'\n')

        self.telnet.read_until(b"$",10)
        self.telnet.write(su.encode('ascii')+b'\n')

        self.telnet.read_until(b"Password:",10)
        self.telnet.write(su_pwd.encode('ascii')+b'\n')
        time.sleep(2)
        login_result = self.telnet.read_very_eager().decode('ascii')
        # print(login_result)

        if '#' in login_result:
            return True
        else:
            print('账号密码错误')
            return False

    def import_content(self,content):
        self.telnet.write(content.encode('ascii')+b'\n')
        time.sleep(2)
        content_result=self.telnet.read_very_eager().decode('ascii')
        return content_result



if __name__ == '__main__':
    host_ip='192.168.1.1'
    username='telnetadmin'
    password='telnetadmin'
    su='su'
    su_pwd='12345678LaYBc'
    telnet_client=TelnetClient()
    if telnet_client.login_host(host_ip,username,password,su,su_pwd):
        free = str(telnet_client.import_content("top -n 1 | grep Mem: | awk '{print $4}'")).split()
        cpu = str(telnet_client.import_content("top -n 1 | grep CPU: | awk '{print $8}'")).split()

        data_excel = data_excel.DataWtExcel()
        data_excel.run_data_excel(crosswise=4,vertical=7,content=6)





