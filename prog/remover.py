import getpass
import os

user = getpass.getuser()

if user == 'root':
    print ("remove package...")
    os.system("apt-get remove rkhunter -y")
    os.system("apt-get remove fail2ban -y")
    os.system("apt-get remove iptables -y")
    os.system("apt-get remove iptables-persistent -y")

else :
    print ("use root")
