import os
from simple_term_menu import TerminalMenu
from yaspin import yaspin


def title () :
    os.system("clear")
    print ('+-------------------------------+')
    print ('|    sec-vps configuration      |')
    print ('|                               |')
    print ('|         By bubudotsh          |')
    print ('+-------------------------------+\n\n')


def setup () :
    with yaspin(text="Downloading package", color="cyan") as sp:

        os.system('apt-get install fail2ban -y > /dev/null')
        sp.write("> 1/4")

        os.system('apt-get install iptables -y > /dev/null')
        sp.write("> 2/4")

        os.system('apt-get install lynis -y > /dev/null')
        sp.write("> 3/4")

        os.system('apt-get install iptables-persistent -y')
        sp.write("> 4/4")

        sp.ok("✔")


def firewall () :
    os.system('rm -fr /etc/init.d/firewall.sh ; cp -fr prog/firewall.txt /etc/init.d/firewall.sh')

    title()
    terminal_menu = TerminalMenu(
        ["HTTP - web server", "FTP - file trensfert", "SMTP - simple mail trensfert", "POP3 - mail receiver", "POP3S - secure mail receiver", "IMAP - mail server", "OVH - if you are on ovh server", "Not"],
        multi_select=True,
        show_multi_select_hint=True,
    )
    menu_entry_indices = terminal_menu.show()

    if 'HTTP - web server' in terminal_menu.chosen_menu_entries :
        httprules1 = "iptables -t filter -A OUTPUT -p tcp --dport 80 -j ACCEPT"
        httprules2 = "iptables -t filter -A INPUT -p tcp --dport 80 -j ACCEPT"
        httprules3 = "iptables -t filter -A OUTPUT -p tcp --dport 443 -j ACCEPT"
        httprules4 = "iptables -t filter -A INPUT -p tcp --dport 443 -j ACCEPT"

        os.system('sed -i "s/# HTTP1/%s/" /etc/init.d/firewall.sh' % httprules1)
        os.system('sed -i "s/# HTTP2/%s/" /etc/init.d/firewall.sh' % httprules2)
        os.system('sed -i "s/# HTTP3/%s/" /etc/init.d/firewall.sh' % httprules3)
        os.system('sed -i "s/# HTTP4/%s/" /etc/init.d/firewall.sh' % httprules4)

    if 'FTP - file trensfert' in terminal_menu.chosen_menu_entries :
        ftprules1 = "iptables -t filter -A OUTPUT -p tcp --dport 20:21 -j ACCEPT"
        ftprules2 = "iptables -t filter -A INPUT -p tcp --dport 20:21 -j ACCEPT"

        os.system('sed -i "s/# FTP1/%s/" /etc/init.d/firewall.sh' % ftprules1)
        os.system('sed -i "s/# FTP2/%s/" /etc/init.d/firewall.sh' % ftprules2)

    if 'SMTP - simple mail trensfert' in terminal_menu.chosen_menu_entries :
        smtprules1 = "iptables -t filter -A INPUT -p tcp --dport 25 -j ACCEPT"
        smtprules2 = "iptables -t filter -A OUTPUT -p tcp --dport 25 -j ACCEPT"

        os.system('sed -i "s/# SMTP1/%s/" /etc/init.d/firewall.sh' % smtprules1)
        os.system('sed -i "s/# SMTP2/%s/" /etc/init.d/firewall.sh' % smtprules2)

    if 'POP3 - mail receiver' in terminal_menu.chosen_menu_entries :
        pop3rules1 = "iptables -t filter -A INPUT -p tcp --dport 110 -j ACCEPT"
        pop3rules2 = "iptables -t filter -A OUTPUT -p tcp --dport 110 -j ACCEPT"

        os.system('sed -i "s/# POP31/%s/" /etc/init.d/firewall.sh' % pop3rules1)
        os.system('sed -i "s/# POP32/%s/" /etc/init.d/firewall.sh' % pop3rules2)

    if 'POP3S - secure mail receiver' in terminal_menu.chosen_menu_entries :
        pop3srules1 = "iptables -t filter -A INPUT -p tcp --dport 995 -j ACCEPT"
        pop3srules2 = "iptables -t filter -A OUTPUT -p tcp --dport 995 -j ACCEPT"

        os.system('sed -i "s/# POP3S1/%s/" /etc/init.d/firewall.sh' % pop3srules1)
        os.system('sed -i "s/# POP3S2/%s/" /etc/init.d/firewall.sh' % pop3srules2)

    if 'IMAP - mail server' in terminal_menu.chosen_menu_entries :
        imaprules1 = "iptables -t filter -A INPUT -p tcp --dport 143 -j ACCEPT"
        imaprules2 = "iptables -t filter -A OUTPUT -p tcp --dport 143 -j ACCEPT"

        os.system('sed -i "s/# IMAP1/%s/" /etc/init.d/firewall.sh' % imaprules1)
        os.system('sed -i "s/# IMAP2/%s/" /etc/init.d/firewall.sh' % imaprules2)

    if 'OVH - if you are on ovh server' in terminal_menu.chosen_menu_entries :
        ovhrules1 = "iptables -A OUTPUT -p tcp --dport 3260 -m state --state NEW,ESTABLISHED -j ACCEPT"

        os.system('sed -i "s/# OVH1/%s/" /etc/init.d/firewall.sh' % ovhrules1)

    if 'Not' in terminal_menu.chosen_menu_entries :
        print ("")

    #
    os.system('chmod +x /etc/init.d/firewall.sh')
    os.system('sudo bash /etc/init.d/firewall.sh')
    os.system('netfilter-persistent save > /dev/null')


def scan_conf () :
    mailsender = input('entrer mail sender, outlook uniquement : ')
    os.system('sed -i "s/sendermail1/%s/g" prog/secvps.py' % mailsender)

    password = input('enter password for mail sender : ')
    os.system('sed -i "s/password1/%s/g" prog/secvps.py' % password)

    mailreciver = input('mail reciver : ')
    os.system('sed -i "s/ricivermail1/%s/g" prog/secvps.py' % mailreciver)


def fail2ban () :
    # https://www.sublimigeek.fr/installer-et-configurer-fail2ban-sur-un-serveur
    print("\nconfiguration of fail2ban\n")

    bantime = input('number of seconds that a host is banned: ')
    os.system('sed -i "s/aaaa/%s/g" f2b/jail.conf  ' % bantime)

    findtime = input('A host is banned if it has generated "maxretry" during the last "findtime": ')
    os.system('sed -i "s/bbbb/%s/g" f2b/jail.conf  ' % findtime)

    maxretry = input('number of failures before a host get banned: ')
    os.system('sed -i "s/cccc/%s/g" f2b/jail.conf ' % maxretry)

    os.system('cp -fr f2b/jail.conf /etc/fail2ban/jail.conf')
    os.system('cp -fr f2b/jail/* /etc/fail2ban/filter.d/')

    os.system('/etc/init.d/fail2ban stop ; /etc/init.d/fail2ban start')


setup()
firewall()
scan_conf()
fail2ban()