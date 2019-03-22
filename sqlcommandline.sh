#/bin/bash
arg=$1
mysql -u root -proot < $arg 2>/dev/null
exit 0


