import getpass
import os
import time
from simple_term_menu import TerminalMenu
from yaspin import yaspin
import datetime
import platform
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# MAKE DEBUG :: AUCUN /DEV/NULL
# MAKE AUDIT FOR PM2

# variables
user = getpass.getuser()

def title () :
    os.system("clear")
    print ('+-------------------------------+')
    print ('|            sec-vps            |')
    print ('|                               |')
    print ('|         By bubudotsh          |')
    print ('+-------------------------------+\n\n')


def scan () :

    with yaspin(text="Scanning...", color="yellow") as spinner:
        os.system('rm -fr src/data/scanlog.txt; src/touch data/scanlog.txt')
        os.system('rm -fr src/data/audit.txt; touch src/data/audit.txt')
        os.system('sudo lynis audit system > src/data/scanlog.txt')
        os.system('sed -i -e "s,\x1B\[[0-9;]*[a-zA-Z],,g" src/data/scanlog.txt')
        spinner.ok("✅")


    #Stats 
    Usage = "Total Usage     : {} %".format(psutil.cpu_percent())
    sys = "System          : {}".format(platform.system())
    node = "Node Name       : {}".format(platform.node())
    release = "Release         : {}".format(platform.release())
    machine = "Machine         : {}".format(platform.machine())
    sysinfo = "\n{}\n{}\n{}\n{}\n{}".format(sys, node, release, machine, Usage)

    audit = open("src/data/audit.txt", 'a')

    audit.write("[ sev-vps result ]\n\n")

    file = open('src/data/scanlog.txt', 'r')
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

    os.system('touch tmp/tmp.txt ; grep "Tests performed" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")

    audit.write("----------------------------------\n")
    os.system('touch tmp/tmp.txt ; grep "Compliance status" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")
    os.system('touch tmp/tmp.txt ; grep "Compliance Status" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")


    os.system('touch tmp/tmp.txt ; grep "Security audit" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")
    os.system('touch tmp/tmp.txt ; grep "Security Audit" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")


    os.system('touch tmp/tmp.txt ; grep "Vulnerability scan" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")
    os.system('touch tmp/tmp.txt ; grep "Vulnerability Scan" src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")


    os.system('touch tmp/tmp.txt ; grep "Firewall          " src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")

    os.system('touch tmp/tmp.txt ; grep "Malware scanner    " src/data/scanlog.txt > tmp/tmp.txt')
    os.system('sed -i -e "s/  - //" tmp/tmp.txt')
    tmp = open('tmp/tmp.txt', 'r')
    read_tmp = tmp.read()
    audit.write(read_tmp)
    tmp.close()
    os.system("rm -fr tmp/tmp.txt")

    audit.write("----------------------------------\n")
    os.system("touch tmp/tmp ; sudo last -4 | awk '{print $1, $3, $5, $6, $7, $9, $10}' | head -n4 > tmp/tmp.txt")
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

    result = open("src/data/audit.txt", 'r')
    res = result.read()
    print("\n", res)


def mail () :
    
    tim = input('\n enter time in hour between 2 scans: ')
    res = int(tim) * 60 * 60

    while True :
        os.system("sudo apt-get update -y ; apt-get upgrade -y")
        os.system("sudo apt update -y ; apt upgrade -y")
        scan()

        fi = open("src/data/audit.txt", 'r')
        s = fi.read()

        #send mail
        msg = MIMEMultipart()
        msg['From'] = 'sendermail1'
        msg['To'] = 'ricivermail1'
        msg['Subject'] = 'sev-vps audit'  
        message = s
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login('sendermail1', 'password1')
        mailserver.sendmail('sendermail1', 'ricivermail1', msg.as_string())
        mailserver.quit()

        print ("mail ok")

        time.sleep(res)

mail()