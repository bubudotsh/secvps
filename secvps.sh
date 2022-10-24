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