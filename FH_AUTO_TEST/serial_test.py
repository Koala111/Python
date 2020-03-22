import serial

ser = serial.Serial('com4', 115200, timeout=0.2)
# 接收返回的信息
recv = ser.readline()
while True:
    print(str(recv))
    if str(recv) == 'q':
        break
		
'''
import serial
import time


def setTout(t):
    print("Old Timeout is:[%s]" % po1.getTimeout())
    po1.setTimeout(t)
    print("New Timeout is:[%s]" % po1.getTimeout())


def sendShell(sp, cmd):
    sp.write(cmd + "\n")
    print("send shell cmd:[%s]" % cmd)
    str = sp.readall()
    return str


def shell_io(sp, cmd, sleepTime):
    str = sendShell(sp, cmd)
    print(str)
    time.sleep(sleepTime)


po1 = serial.Serial('com4', 115200)
timeStart = time.time()
portnow = po1.portstr
print("COM port now is:[%s]" % portnow)
setTout(5)

shell_io(po1, "ls", 2)

shell_io(po1, "pwd", 2)

shell_io(po1, "ls -l", 2)

po1.close()
'''