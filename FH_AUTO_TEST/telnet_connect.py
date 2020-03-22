import sys
import telnetlib
import subprocess
COLOR_GREEN="\033[0;32;40m"
COLOR_RED="\033[0;31;40m"
COLOR_YELLOW="\033[0;33;40m"
COLOR_RSET="\033[0m"
def get_green_str(raw_str):
    return COLOR_GREEN + raw_str + COLOR_RSET
def get_red_str(raw_str):
    return COLOR_RED + raw_str + COLOR_RSET
def get_yellow_str(raw_str):
    return COLOR_YELLOW + raw_str + COLOR_RSET
def mock_telnet(ip, port):
    try:
        tn = telnetlib.Telnet(ip, port)
        print("address:" + str(ip) + ":" + str(port) + get_green_str(" : connect successfuly"))
    except:
        print("address:" + str(ip) + ":" + str(port) + get_red_str(" : connect failed"))
def mock_netstat():
    sub = subprocess.Popen("netstat -atpn", shell=True, stdout=subprocess.PIPE)
    output_array = []
    while True:
        line = sub.stdout.readline()
        if not line:
            break
        output_array.append(line)
    sub.wait()
    sub.stdout.close()
    return output_array
def main():
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        port = input("please input port")
    elif len(sys.argv) == 3:
        ip = sys.argv[1]
        port = sys.argv[2]
    else:
      print(get_red_str("[ERROR] please input ip and port"))
      return
    mock_telnet(ip, port)
    out_array = mock_netstat()
    for i in range (0, len(out_array)):
        print( i, out_array[i].strip("\n"))
if __name__ == "__main__":
    main()  