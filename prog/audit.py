import getpass
import os
import time
from simple_term_menu import TerminalMenu
from yaspin import yaspin
import datetime
import platform
import psutil
import smtplib


os.system("clear")
print ('+-------------------------------+')
print ('|            sec-vps            |')
print ('|                               |')
print ('|         By bubudotsh          |')
print ('+-------------------------------+\n\n')




with yaspin(text="Scanning...", color="yellow") as spinner:
    os.system('rm -fr data/scanlog.txt; touch data/scanlog.txt')
    os.system('rm -fr data/audit.txt; touch data/audit.txt')
    os.system('sudo lynis audit system > data/scanlog.txt')
    os.system('sed -i -e "s,\x1B\[[0-9;]*[a-zA-Z],,g" data/scanlog.txt')
    spinner.ok("✅")


#Stats 
Usage = "Total Usage     : {} %".format(psutil.cpu_percent())
sys = "System          : {}".format(platform.system())
node = "Node Name       : {}".format(platform.node())
release = "Release         : {}".format(platform.release())
machine = "Machine         : {}".format(platform.machine())
sysinfo = "\n{}\n{}\n{}\n{}\n{}".format(sys, node, release, machine, Usage)

audit = open("data/audit.txt", 'a')

audit.write("[ sev-vps result ]\n\n")

file = open('data/scanlog.txt', 'r')
read_data = file.read()

audit.write("----------------------------------")
audit.write(sysinfo)
audit.write("\n----------------------------------\n")

per_word = read_data.split('WARNING')
audit.write("Warnings        : ")
audit.write(str(len(per_word)))
audit.write("\n")

per_word1 = read_data.split('SUGGESTION')
audit.write("Suggestion      : ")
audit.write(str(len(per_word1)))
audit.write("\n")

os.system('touch tmp/tmp.txt ; grep "Tests performed" data/scanlog.txt > tmp/tmp.txt')
os.system('sed -i -e "s/  //" tmp/tmp.txt')
tmp = open('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system("rm -fr tmp/tmp.txt")

audit.write("----------------------------------\n")
os.system('touch tmp/tmp.txt ; grep "Compliance Status" data/scanlog.txt > tmp/tmp.txt ; rep "Compliance status" data/scanlog.txt > tmp/tmp.txt')
os.system('sed -i -e "s/  - //" tmp/tmp.txt')
tmp = open('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system("rm -fr tmp/tmp.txt")

os.system('touch tmp/tmp.txt ; grep "Security Audit" data/scanlog.txt > tmp/tmp.txt ; grep "Security audit" data/scanlog.txt > tmp/tmp.txt')
os.system('sed -i -e "s/  - //" tmp/tmp.txt')
tmp = open('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system("rm -fr tmp/tmp.txt")

os.system('touch tmp/tmp.txt ; grep "Vulnerability Scan" data/scanlog.txt > tmp/tmp.txt ; grep "Vulnerability scan" data/scanlog.txt > tmp/tmp.txt')
os.system('sed -i -e "s/  - //" tmp/tmp.txt')
tmp = open('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system("rm -fr tmp/tmp.txt")

os.system('touch tmp/tmp.txt ; grep "Firewall          " data/scanlog.txt > tmp/tmp.txt')
os.system('sed -i -e "s/  - //" tmp/tmp.txt')
tmp = open('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system("rm -fr tmp/tmp.txt")

os.system('touch tmp/tmp.txt ; grep "Malware scanner    " data/scanlog.txt > tmp/tmp.txt')
os.system('sed -i -e "s/  - //" tmp/tmp.txt')
tmp = open('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system("rm -fr tmp/tmp.txt")

audit.write("----------------------------------\n")
os.system("touch tmp/tmp ; sudo last -4 | awk '{print $1, $3, $4, $5, $6, $7, $9, $10}' | head -n4 > tmp/tmp.txt")
tmp = open ('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system('rm -fr tmp/tmp.txt')

audit.write("----------------------------------\n")

os.system('touch tmp/tmp ; sudo fail2ban-client status > tmp/tmp.txt')
os.system('sed -i -e "s/|//" tmp/tmp.txt')
tmp = open ('tmp/tmp.txt', 'r')
read_tmp = tmp.read()
audit.write(read_tmp)
tmp.close()
os.system('rm -fr tmp/tmp.txt')

audit.write("----------------------------------\n")
audit.write("log of scan     : sec-vps/data/logscan.txt\naudit file      : sec-vps/data/audit.txt")
audit.write("\n----------------------------------\n")

date1 = datetime.datetime.now()
date2 = "- Date of scan: " + date1.strftime('%Y-%m-%d %H:%M:%S')
audit.write(date2)
audit.close()

result = open("data/audit.txt", 'r')
res = result.read()
print("\n", res)