help () {
    echo "NAME"
    echo "      secvps.sh - Secure your server and create security audits on linux"
    echo " "
    echo " "
    echo "SYNOPSIS"
    echo "      sudo ./secvps.sh OPTION"
    echo " "
    echo "DESCRIPTION"
    echo "      This script secures your Linux server:"
    echo " "
    echo "      - configuration of a firewall"
    echo "      - manage port connections with fail2ban"
    echo "      - create audits with Lynis"
    echo " "
    echo "      It also sends you a security audit report via email on a recurring basis"
    echo " "
    echo "OPTIONS"
    echo "      -h      help"
    echo "      -d      make audit with debug"
    echo "      -a      make audit"
    echo "      -l      create an audit every x hour and send the report by email"
    echo " "
    echo "AUTHOR"
    echo "      Developped by bubudotsh"
    echo " "
    exit
}



# Option
while getopts "hdal" option; do
case $option in
    h)
        help
        exit;;
    d)
        debug
        exit;;
    a)
        sudo python3 src/audit.py
        exit;;
    l)
        sudo python3 src/secvps.py
        exit;;
    \?)
        echo "bad option, help : -h"
        exit;;
    esac
done

echo "enter Option, see -h"