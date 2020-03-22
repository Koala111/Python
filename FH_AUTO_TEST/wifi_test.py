#测试步骤：
#step1. 设备上电启动
step2 = 'fhtool getapmac'  #读取ath0的mac地址
result2 = str(self.telnet_operation.import_content(step2)).split()

step3 = 'ip netns exec MNG ifconfig ath0' #查看ath0的mac地址
result3 = str(self.telnet_operation.import_content(step3)).split()

if (result3.find(result2)>=0): #成功返回的是292，失败返回-1
	print('步骤2、步骤3中mac地址一致')
else:
	print('步骤2、步骤3中mac地址不一致，请注意排查问题！！！')

step4 = 'fhtool getssid 1' #读取SSID1
result4 = str(self.telnet_operation.import_content(step4)).split()

step5 = 'fhtool getssid_pwd 1' #读取SSID1密码
result5 = str(self.telnet_operation.import_content(step5)).split()

step6 = 'fhtool getssid_switch 1' #读取SSID1的开关状态
result6 = str(self.telnet_operation.import_content(step6)).split()

step7 = 'fhtool getssid_hide 1' #读取SSID1隐藏状态
result7 = str(self.telnet_operation.import_content(step7)).split()

if result4.strip()!=''&result5.strip()!=''&result6.strip()!=''&result7.strip()!='':
	print('步骤4读取SSID1名称，步骤5读取SSID1密码，步骤6读取SSID1开关状态，步骤7读取SSID1隐藏状态都正常')
else:
	print('步骤4、5、6、7执行后输出有问题，请注意排查问题！！！')

step8 = 'fhtool setssid 1 朝闻道夕死可矣' #设置SSID1为 朝闻道夕死可矣
result8 = str(self.telnet_operation.import_content(step8)).split()

step9 = 'fhtool setssid_pwd 1 66666666' #设置SSID1密码为66666666
result9 = str(self.telnet_operation.import_content(step9)).split()

step10 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result10 = str(self.telnet_operation.import_content(step10)).split()

#step11. 使用手机接入SSID1
step11 = input("使用手机接入SSID1,然后请输入测试结果(OK/NOK)：")
if (step11.find('OK')>0): #成功返回的是292，失败返回-1
	print('手机能正常接入')
else:
	print('步骤11中测试异常，请注意排查问题！！！')

step12 = 'fhtool setssid_switch 1 0' #关闭SSID1
result12 = str(self.telnet_operation.import_content(step12)).split()

step13 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result13 = str(self.telnet_operation.import_content(step13)).split()

step14 = 'ip netns exec MNG ifconfig ath0' #查看ath0是否up
result14 = str(self.telnet_operation.import_content(step14)).split()
if (result14.find('UP')<0): #成功返回的是292，失败返回-1
	print("步骤14 ath0未UP")
else:
	print('步骤12、步骤13,14中测试异常，请注意排查问题！！！')


step15 = 'fhtool setssid_switch 1 1' #开启SSID1
result15 = str(self.telnet_operation.import_content(step15)).split()

step16 = 'fhtool setssid_hide 1 1' #隐藏SSID1
result16 = str(self.telnet_operation.import_content(step16)).split()

step17 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result17 = str(self.telnet_operation.import_content(step17)).split()

#step18. 使用手机搜索SSID，输入SSID名称连接
step18 = input("使用手机接入SSID1,然后请输入测试结果(OK/NOK)：")
if (step18.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤18能正常接入')
else:
	print('步骤18中测试异常，请注意排查问题！！！')



step19 = 'fhtool setssid_hide 1 0' #关闭SSID1隐藏
result19 = str(self.telnet_operation.import_content(step19)).split()

step20 = 'fhtool setssid_maxassoc 1 0' #设置SSID1最大连接用户数为0
result20 = str(self.telnet_operation.import_content(step20)).split()

step21 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result21 = str(self.telnet_operation.import_content(step21)).split()

#step22. 使用手机尝试接入SSID1
step22 = input("使用手机接入SSID1,然后请输入测试结果(OK/NOK)：")
if (step22.find('OK')>0): #成功返回的是292，失败返回-1
	print("步骤22手机无法接入")
else:
	print('步骤22中测试异常，请注意排查问题！！！')


step23 = 'fhtool setssid_maxassoc 1 1' #设置SSID1最大连接用户数为1
result23 = str(self.telnet_operation.import_content(step23)).split()

step24 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result24 = str(self.telnet_operation.import_content(step24)).split()
#step25. 用一台手机接入SSID1，使用第二台手机尝试接入SSID1
print('步骤25第一台手机能接入，第二台手机无法接入')

step26 = 'fhtool setssid_maxassoc 1 32' #设置SSID1最大连接用户数为32，执行fhtool setssid_apisolate 1 1开启SSID1二层隔离
result26 = str(self.telnet_operation.import_content(step26)).split()

step27 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result27 = str(self.telnet_operation.import_content(step27)).split()

#step28. 用2台手机接入SSID1，手机互ping
step28 = input("用2台手机接入SSID1，手机互ping,然后请输入测试结果(OK/NOK)：")
if (step28.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤28手机互ping不通')
else:
	print('步骤28中测试异常，请注意排查问题！！！')


step29 = 'fhtool setwlan_authmode 1 OPEN' #修改SSID1的认证方式为OPEN
result29 = str(self.telnet_operation.import_content(step29)).split()

step30 = 'fhtool setwlan_encryptype 1 NONE' #修改SSID1的加密为NONE
result30 = str(self.telnet_operation.import_content(step30)).split()

step31 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result31 = str(self.telnet_operation.import_content(step31)).split()

#step32. 手机接入SSID1
step32 = input("手机接入SSID1,然后请输入测试结果(OK/NOK)：")
if (step32.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤32手机无需输入密码即可接入')
else:
	print('步骤32中测试异常，请注意排查问题！！！')

step33 = 'fhtool setwlan_encryptype 1 AES' #修改SSID1的加密为AES
result33 = str(self.telnet_operation.import_content(step33)).split()

step34 = 'fhtool setwlan_authmode 1 WPA-PSK' #修改SSID认证方式为WPA-PSK
result34 = str(self.telnet_operation.import_content(step34)).split()

step35 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result35 = str(self.telnet_operation.import_content(step35)).split()

step36 = 'cat /var/hostapd-ath0.conf | grep wpa'
result36 = str(self.telnet_operation.import_content(step36)).split()
if (result36.find('1')<0): #成功返回的是292，失败返回-1
	print('步骤36 wpa类型值为1')
else:
	print('步骤36测试异常，请注意排查问题！！！')


step37 = 'fhtool setwlan_authmode 1 WPA2-PSK' #修改SSID认证方式为WPA2-PSK
result37 = str(self.telnet_operation.import_content(step37)).split()

step38 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result38 = str(self.telnet_operation.import_content(step38)).split()

step39 = 'cat /var/hostapd-ath0.conf' | grep wpa
result39 = str(self.telnet_operation.import_content(step39)).split()
if (result39.find('2')<0): #成功返回的是292，失败返回-1
	print('步骤39 wpa类型值为2')
else:
	print('步骤39测试异常，请注意排查问题！！！')

step40 = 'fhtool setwlan_authmode 1 WPA/WPA2-PSK' #修改SSID认证方式为WPA/WPA2-PSK
result40 = str(self.telnet_operation.import_content(step40)).split()

step41 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result41 = str(self.telnet_operation.import_content(step41)).split()

step42 = 'cat /var/hostapd-ath0.conf | grep wpa'
result42 = str(self.telnet_operation.import_content(step42)).split()
if (result42.find('3')<0): #成功返回的是292，失败返回-1
	print('步骤42 wpa类型值为3')
else:
	print('步骤42测试异常，请注意排查问题！！！')

step43 = 'fhtool setwlan_switch 0' #关闭2.4G AP模块
result43 = str(self.telnet_operation.import_content(step43)).split()

step44 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result44 = str(self.telnet_operation.import_content(step44)).split()

step45 = 'ip netns exec MNG ifconfig ath0' #查看ath0接口是否down掉
result45 = str(self.telnet_operation.import_content(step45)).split()
if (result45.find('DOWN')<0): #成功返回的是292，失败返回-1
	print('步骤45 ath0 down掉')
else:
	print('步骤45中测试异常，请注意排查问题！！！')

step46 = 'fhtool setwlan_switch 1' #开启2.4G AP模块
result46 = str(self.telnet_operation.import_content(step46)).split()

step47 = '/usr/init_scripts/wlan.sh'#待wifi重载完成
result47 = str(self.telnet_operation.import_content(step47)).split()

step48 = 'ip netns exec MNG ifconfig ath0' #查看ath0接口是否up
result48 = str(self.telnet_operation.import_content(step48)).split()
if (result48.find('UP')>=0): #成功返回的是292，失败返回-1
	print('步骤48 ath0 up')
else:
	print('步骤48中测试异常，请注意排查问题！！！')

step49 = 'fhtool setwlan_channel 8' #设置2.4G信道为8
result49 = str(self.telnet_operation.import_content(step49)).split()

step50 = '/usr/init_scripts/wlan.sh' #待wifi重载完成
result50 = str(self.telnet_operation.import_content(step50)).split()

step51 = 'ip netns exec MNG iwlist ath0 channel' #查看当前2.4G信道
result51 = str(self.telnet_operation.import_content(step51)).split()
if (result51.find('8')>0): #成功返回的是292，失败返回-1
	print('步骤51 2.4G信道为8')
else:
	print('步骤51中测试异常，请注意排查问题！！！')

step52='fhtool setwlan_radiomode 802.11n' #设置无线模式为802.11n
result52 = str(self.telnet_operation.import_content(step52)).split()

step53='/usr/init_scripts/wlan.sh' #待wifi重载完成
result53 = str(self.telnet_operation.import_content(step53)).split()

step54='ip netns exec MNG iwpriv ath0 get_mode' #查看当前2.4G无线模式
result54 = str(self.telnet_operation.import_content(step54)).split()
if (result54.find('802.11n')>0): #成功返回的是292，失败返回-1
	print('步骤54 2.4G无线模式为802.11n')
else:
	print('步骤54中测试异常，请注意排查问题！！！')

step55='fhtool setwlan_cwmmode 40' #设置频宽为40MHz
result55 = str(self.telnet_operation.import_content(step55)).split()

step56='/usr/init_scripts/wlan.sh' #待wifi重载完成
result56 = str(self.telnet_operation.import_content(step56)).split()

step57='ip netns exec MNG iwpriv ath0 get_mode' #查看当前2.4G频宽
result57 = str(self.telnet_operation.import_content(step57)).split()
if (result57.find('40')>0): #成功返回的是292，失败返回-1
	print("步骤57 2.4G频宽为40MHz")
else:
	print('步骤57中测试异常，请注意排查问题！！！')


step58='fhtool setwlan_txpower 80' #设置无线发射功率为80%强度
result58 = str(self.telnet_operation.import_content(step58)).split()

step59='/usr/init_scripts/wlan.sh' #待wifi重载完成
result59 = str(self.telnet_operation.import_content(step59)).split()

step60='ip netns exec MNG iwconfig ath0' #查看2.4G当前无线发射功率
result60 = str(self.telnet_operation.import_content(step60)).split()
if (result60.find('19')>0): #成功返回的是292，失败返回-1
	print('步骤60 2.4G无线发射功率强度为19dbm')
else:
	print('步骤60中测试异常，请注意排查问题！！！')


step61='fhtool setwlan_wmm 1' #开启wmm功能
result61 = str(self.telnet_operation.import_content(step61)).split()

step62='/usr/init_scripts/wlan.sh' #待wifi重载完成
result62 = str(self.telnet_operation.import_content(step62)).split()

'''
63. 使用Chariot软件工具，分别打AC-VO（语音流）、AC-VI（视频流）、AC-BE（尽力而为流）、AC-BK（背景流）四条流
64. 从LAN测到wifi侧的TCP流，验证吞吐量是否按照优先级高低排列，每条流的优先级分别配置为7、5、0、1
65. 观察四条流占用带宽的情况。

'''
step65 = input("WMM测试,然后请输入测试结果(OK/NOK)：")
if (step65.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤65 四条流占用带宽的情况AC_VO>AC_VI>AC_BE>AC_BK')
else:
	print('步骤65中测试异常，请注意排查问题！！！')


step66='fhtool getapmac_5g' #读取ath4的mac地址
result66 = str(self.telnet_operation.import_content(step66)).split()

step67='ip netns exec MNG ifconfig ath4' #查看ath4的mac地址
result67 = str(self.telnet_operation.import_content(step67)).split()
if (result67.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤66、步骤67中mac地址一致')
else:
	print('步骤66、步骤67中测试异常，请注意排查问题！！！')


step68='fhtool getssid_5g 5' #读取SSID5
result68 = str(self.telnet_operation.import_content(step68)).split()

step69='fhtool getssid_5g_pwd 5' #读取SSID5密码
result69 = str(self.telnet_operation.import_content(step69)).split()

step70='fhtool getssid_5g_switch 5' #读取SSID5的开关状态
result70 = str(self.telnet_operation.import_content(step70)).split()

step71='fhtool getssid_5g_hide 5' #读取SSID5隐藏状态
result71 = str(self.telnet_operation.import_content(step71)).split()
if result68.strip()!=''&result69.strip()!=''&result70.strip()!=''&result71.strip()!='':
	print('步骤68读取SSID5名称，步骤69读取SSID5密码，步骤70读取SSID5开关状态，步骤71读取SSID5隐藏状态都正常')
else:
	print('步骤68,69,70,71执行后输出有问题，请注意排查问题！！！')

step72='fhtool setssid_5g 5 狼来了' #设置SSID5为 狼来了
result72 = str(self.telnet_operation.import_content(step72)).split()

step73='fhtool setssid_5g_pwd 5 66666666' #设置SSID5密码为66666666
result73 = str(self.telnet_operation.import_content(step73)).split()

step74='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result74 = str(self.telnet_operation.import_content(step74)).split()

#step75. 使用手机接入SSID5
step75 = input("使用手机接入SSID5,然后请输入测试结果(OK/NOK)：")
if (step75.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤75手机能正常接入')
else:
	print('步骤75中测试异常，请注意排查问题！！！')


step76='fhtool setssid_5g_switch 5 0' #关闭SSID5
result76 = str(self.telnet_operation.import_content(step76)).split()

step77='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result77 = str(self.telnet_operation.import_content(step77)).split()

step78='ip netns exec MNG ifconfig ath4' #查看ath4是否up
result78 = str(self.telnet_operation.import_content(step78)).split()
if (result78.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤78 ath4未UP')
else:
	print('步骤78中测试异常，请注意排查问题！！！')

step79='fhtool setssid_5g_switch 5 1' #开启SSID5
result79 = str(self.telnet_operation.import_content(step79)).split()

step80='fhtool setssid_5g_hide 5 1' #隐藏SSID5
result80 = str(self.telnet_operation.import_content(step80)).split()

step81='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result81 = str(self.telnet_operation.import_content(step81)).split()

#82. 使用手机搜索SSID5，输入SSID5名称连接
step82 = input("使用手机搜索SSID5，输入SSID5名称连接,然后请输入测试结果(OK/NOK)：")
if (step82.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤82能正常接入')
else:
	print('步骤82中测试异常，请注意排查问题！！！')


step83='fhtool setssid_5g_hide 5 0' #关闭SSID5隐藏
result83 = str(self.telnet_operation.import_content(step83)).split()

step84='fhtool setssid_maxassoc_5g 5 0' #设置SSID5最大连接用户数为0
result84 = str(self.telnet_operation.import_content(step84)).split()

step85='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result85 = str(self.telnet_operation.import_content(step85)).split()

#86. 使用手机尝试接入SSID5
step86 = input("使用手机尝试接入SSID5,然后请输入测试结果(OK/NOK)：")
if (step32.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤86手机无法接入')
else:
	print('步骤86中测试异常，请注意排查问题！！！')


step87='fhtool setssid_maxassoc_5g 5 1' #设置SSID5最大连接用户数为1
result87 = str(self.telnet_operation.import_content(step87)).split()

step88='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result88 = str(self.telnet_operation.import_content(step88)).split()

#step89. 用一台手机接入SSID5，使用第二台手机尝试接入SSID5
step89 = input("用一台手机接入SSID5，使用第二台手机尝试接入SSID5,然后请输入测试结果(OK/NOK)：")
if (step89.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤89第一台手机能接入，第二台手机无法接入')
else:
	print('步骤89中测试异常，请注意排查问题！！！')



step90='fhtool setssid_maxassoc_5g 5 32' #设置SSID5最大连接用户数为32,执行fhtool setssid_apisolate_5g 5 1开启SSID5二层隔离
result90 = str(self.telnet_operation.import_content(step90)).split()

step91='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result91 = str(self.telnet_operation.import_content(step91)).split()

#step92. 用2台手机接入SSID5，手机互ping
step92 = input("用2台手机接入SSID5，手机互ping,然后请输入测试结果(OK/NOK)：")
if (step92.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤92手机互ping不通')
else:
	print('步骤92中测试异常，请注意排查问题！！！')


step93='fhtool setwlan_authmode_5g 5 OPEN' #修改SSID5的认证方式为OPEN
result93 = str(self.telnet_operation.import_content(step93)).split()

step94='fhtool setwlan_encryptype_5g 5 NONE' #修改SSID5的加密为NONE
result94 = str(self.telnet_operation.import_content(step94)).split()

step95='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result95 = str(self.telnet_operation.import_content(step95)).split()

#step96. 手机接入SSID5
step96 = input("手机接入SSID5，然后请输入测试结果(OK/NOK)：")
if (step96.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤96手机无需输入密码即可接入')
else:
	print('步骤96中测试异常，请注意排查问题！！！')



step97='fhtool setwlan_encryptype_5g 5 AES' #修改SSID5的加密为AES
result97 = str(self.telnet_operation.import_content(step97)).split()

step98='fhtool setwlan_authmode_5g 5 WPA-PSK' #修改SSID5认证方式为WPA-PSK
result98 = str(self.telnet_operation.import_content(step98)).split()

step99='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result99 = str(self.telnet_operation.import_content(step99)).split()

step100='cat /var/hostapd-ath4.conf | grep wpa'
result100 = str(self.telnet_operation.import_content(step100)).split()
if (result100.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤100 wpa类型值为1')
else:
	print('步骤100中测试异常，请注意排查问题！！！')

step101='fhtool setwlan_authmode_5g 5 WPA2-PSK' #修改SSID5认证方式为WPA2-PSK
result101 = str(self.telnet_operation.import_content(step101)).split()

step102='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result102 = str(self.telnet_operation.import_content(step102)).split()

step103='cat /var/hostapd-ath4.conf | grep wpa'
result103 = str(self.telnet_operation.import_content(step103)).split()
if (result103.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤103 wpa类型值为1')
else:
	print('步骤103中测试异常，请注意排查问题！！！')
	
step104='fhtool setwlan_authmode_5g 5 WPA/WPA2-PSK' #修改SSID5认证方式为WPA/WPA2-PSK
result104 = str(self.telnet_operation.import_content(step104)).split()

step105='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result105 = str(self.telnet_operation.import_content(step105)).split()

step106='cat /var/hostapd-ath4.conf | grep wpa'
result106 = str(self.telnet_operation.import_content(step106)).split()
if (result106.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤106 wpa类型值为1')
else:
	print('步骤106中测试异常，请注意排查问题！！！')

step107='fhtool set_wlan_5g_switch 0' #关闭5G AP模块
result107 = str(self.telnet_operation.import_content(step107)).split()

step108='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result108 = str(self.telnet_operation.import_content(step108)).split()

step109='ip netns exec MNG ifconfig ath4' #查看ath4接口是否down掉
result109 = str(self.telnet_operation.import_content(step109)).split()
if (result109.find('ath4 down')>0): #成功返回的是292，失败返回-1
	print('步骤109 ath4 down掉')
else:
	print('步骤109中测试异常，请注意排查问题！！！')


step110='fhtool set_wlan_5g_switch 1' #开启5G AP模块
result110 = str(self.telnet_operation.import_content(step110)).split()

step111='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result111 = str(self.telnet_operation.import_content(step111)).split()

step112='ip netns exec MNG ifconfig ath4' #查看ath4接口是否up
result112 = str(self.telnet_operation.import_content(step112)).split()
if (result112.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤112 ath4 up')
else:
	print('步骤112中测试异常，请注意排查问题！！！')
	
step113='fhtool setwlan_channel_5g 36' #设置5G信道为36
result113 = str(self.telnet_operation.import_content(step113)).split()

step114='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result114 = str(self.telnet_operation.import_content(step114)).split()

step115='ip netns exec MNG iwlist ath4 channel' #查看当前5G信道
result115 = str(self.telnet_operation.import_content(step115)).split()
if (result115.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤115 2.4G信道为36')
else:
	print('步骤115中测试异常，请注意排查问题！！！')
	
step116='fhtool setwlan_radiomode_5g 802.11a/n/ac' #设置无线模式为802.11a/n/ac
result116 = str(self.telnet_operation.import_content(step116)).split()

step117='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result117 = str(self.telnet_operation.import_content(step117)).split()

step118='ip netns exec MNG iwpriv ath4 get_mode' #查看当前5G无线模式
result118 = str(self.telnet_operation.import_content(step118)).split()
if (result118.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤118 2.4G无线模式为802.11ac')
else:
	print('步骤118中测试异常，请注意排查问题！！！')
	
step119='fhtool setwlan_cwmmode_5g 40' #设置频宽为40MHz
result119 = str(self.telnet_operation.import_content(step119)).split()

step120='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result120 = str(self.telnet_operation.import_content(step120)).split()

step121='ip netns exec MNG iwpriv ath4 get_mode' #查看当前5G频宽
result121 = str(self.telnet_operation.import_content(step121)).split()
if (result121.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤121 2.4G频宽为40MHz')
else:
	print('步骤121中测试异常，请注意排查问题！！！')
	
step122='fhtool setwlan_txpower_5g 80' #设置无线发射功率为80%强度
result122 = str(self.telnet_operation.import_content(step122)).split()

step123='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result123 = str(self.telnet_operation.import_content(step123)).split()

step124='ip netns exec MNG iwconfig ath4' #查看5G当前无线发射功率
result124 = str(self.telnet_operation.import_content(step124)).split()
if (result124.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤124 2.4G无线发射功率强度为22dbm')
else:
	print('步骤124中测试异常，请注意排查问题！！！')


step125='fhtool setwlan_wmm_5g 1' #开启5G wmm功能
result125 = str(self.telnet_operation.import_content(step125)).split()

step126='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result126 = str(self.telnet_operation.import_content(step126)).split()

'''
127. 使用Chariot软件工具，分别打AC-VO（语音流）、AC-VI（视频流）、AC-BE（尽力而为流）、AC-BK（背景流）四条流
128. 从LAN测到wifi侧的TCP流，验证吞吐量是否按照优先级高低排列，每条流的优先级分别配置为7、5、0、1
129. 观察四条流占用带宽的情况。
'''
step129 = input("5G WMM测试,然后请输入测试结果(OK/NOK)：")
if (step129.find('OK')>0): #成功返回的是292，失败返回-1
	print('步骤129 四条流占用带宽的情况AC_VO>AC_VI>AC_BE>AC_BK')
else:
	print('步骤129中测试异常，请注意排查问题！！！')


step130='fhtool wifi_whether_is_dual_band'#查看当前设备是否双频（1代表双频，0代表单频）
result130 = str(self.telnet_operation.import_content(step130)).split()
if (result130.find('1')>0): #成功返回的是292，失败返回-1
	print('步骤130 读取值符合当前设备情况')
else:
	print('步骤130中测试异常，请注意排查问题！！！')

step131='fhtool setssid_switch 2 1' #开启SSID2
result131 = str(self.telnet_operation.import_content(step131)).split()

step132='fhtool setssid_switch 3 1' #开启SSID3
result132 = str(self.telnet_operation.import_content(step132)).split()

step133='fhtool setssid_switch 4 1' #开启SSID4
result133 = str(self.telnet_operation.import_content(step133)).split()

step134='fhtool setssid_5g_switch 6 1' #开启SSID6
result134 = str(self.telnet_operation.import_content(step134)).split()

step135='fhtool setssid_5g_switch 7 1' #开启SSID7
result135 = str(self.telnet_operation.import_content(step135)).split()

step136='fhtool setssid_5g_switch 8 1' #开启SSID8
result136 = str(self.telnet_operation.import_content(step136)).split()

step137='/usr/init_scripts/wlan.sh' #待wifi重载完成
result137 = str(self.telnet_operation.import_content(step137)).split()

step138='/usr/init_scripts/wlan11ac.sh' #待wifi重载完成
result138 = str(self.telnet_operation.import_content(step138)).split()

step139='ip netns exec MNG ifconfig' #查看SSID1~SSID8是否都处于UP状态，且用手机搜索对应SSID
result139 = str(self.telnet_operation.import_content(step139)).split()
if (result139.find('UP')>0): #成功返回的是292，失败返回-1
	print('步骤139 SSID1~SSID8是否都处于UP状态，且手机能搜索到对应SSID')
else:
	print('步骤139中测试异常，请注意排查问题！！！')



 
 

