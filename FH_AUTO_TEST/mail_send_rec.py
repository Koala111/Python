
'''
pip install yagmail keyring schedule imbox
schedule  #定时任务管理器
启用IMAP
smtp.163.com
smtp.163.com 

'''
import csv
import time
import requests
import yagmail
import keyring
from imbox import Imbox
url1 = r'https://free-api.heweather.net/s6/weather/forecast?location=武汉&key=a1bf3eef06a64f39b31f568c4a431ca0'
url2 = r'https://free-api.heweather.net/s6/weather/forecast?location=襄阳&key=a1bf3eef06a64f39b31f568c4a431ca0'
# 获取当日时间	2019-11-10
today_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
url_list=[url1,url2]
def get_weather_data(url):
    
    res = requests.get(url).json()
    # res.encoding = 'utf-8'
    result = res['HeWeather6'][0]['daily_forecast']
    location = res['HeWeather6'][0]['basic']
    city = location['admin_area'] + location['location']
    names = ['城市', '时间', '天气状况', '最高温', '最低温', '日出', '日落']
    with open('today_weather.csv', 'a+', newline='')as f:
        writer = csv.writer(f)
        #reader = csv.reader(f)
        '''
        reader = csv.DictReader(f)
        print(reader)
        column = [row['城市'] for row in reader]
        print(column)
        #if column[1] == NULL:
        '''
        writer.writerow(names)
        for data in result:
            date = data['date']
            cond = data['cond_txt_d']
            max = data['tmp_max']
            min = data['tmp_min']
            sr = data['sr']
            ss = data['ss']
            writer.writerows([(city, date, cond, max, min, sr, ss)])
for url in url_list:
	get_weather_data(url)
#yagmail.register('18846087935@163.com','qq123456') #这个在交互式里面执行，后面会保存
yag = yagmail.SMTP(user='18846087935@163.com',host='smtp.163.com')
contents=[
			'这里是一段正文内容',
			'这里是一段正文内容',
			'<a href="https://www.baidu.com">百度 </a>',
			'today_weather.csv'
		]
#yag.send(['18846087935@163.com'],'这是一封邮件',contents) #自己发送给自己查看

'''
#http://config.mail.163.com/settings/imap/index.jsp?uid=18846087935@163.com
password = keyring.get_password('yagmail','18846087935@163.com')
with Imbox('imap.163.com','18846087935@163.com',password,ssl=True) as imbox:
	
	unread_inbox_messages = imbox.message(unread=True)#所有未读邮件
	unread_inbox_messages = imbox.message(flagged=True)#所有未读邮件
	unread_inbox_messages = imbox.message(sent_from='')#所有未读邮件
	date_lt.datetime.date(2019,10,3)
	date_gt
	date_on
	if 满足某种条件 imbox.mark_seen(uid)
		imbox.delete(uid)
	
	all_inbox_messages = imbox.messages()#所有邮件
	for uid,message in all_inbox_messages:
		print(message.subject)
		
		print(message.sent_from)
		print(message.sent_to)
		print(message.date)
		print(message.body['html'])
		print(message.attachments)#附件
		print(message.body['plain'])
# coding=gbk
import csv
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
		
def send_email():
    # 设置邮箱的域名
    HOST = 'mail.163.com'
    # 设置邮件标题
    SUBJECT = '%s日份天气预报信息，请查收'%today_time
    # 设置发件人邮箱
    FROM = '18846087935@163.com'
    # 设置收件人邮箱
    TO = 'daix@fiberhome.com'		# 可以同时发送到多个邮箱
    message = MIMEMultipart('related')
    # --------------------------------------发送文本-----------------
	# 发送邮件正文到对方的邮箱中
    message_html = MIMEText("%s日份天气预报到账啦，请查收" % today_time, 'plain', 'utf-8')
    message.attach(message_html)

    # -------------------------------------添加文件---------------------
    # today_weather.csv这个文件
    message_xlsx = MIMEText(open('today_weather.csv', 'rb').read(), 'base64', 'utf-8')
    # 设置文件在附件当中的名字
    message_xlsx['Content-Disposition'] = 'attachment;filename="today_weather.csv"'
    message.attach(message_xlsx)

    # 设置邮件发件人
    message['From'] = FROM
    # 设置邮件收件人
    message['To'] = TO
    # 设置邮件标题
    message['Subject'] = SUBJECT

    # 获取简单邮件传输协议的证书
    email_client = smtplib.SMTP_SSL(host='mail.163.com')
    # 设置发件人邮箱的域名和端口，端口为465
    email_client.connect(HOST, '465')
    # ---------------------------邮箱授权码------------------------------
    result = email_client.login(FROM, 'qq19940211')
    print('登录结果', result)
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
    # 关闭邮件发送客户端
    email_client.close()
'''	
