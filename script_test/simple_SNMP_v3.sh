#!/bin/bash

# snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 sysLocation.0
snmpwalk -v3 -l authPriv -u $2 -a $3 -A $4 -x $5 -X $6 $1 $7 \
| while read line; do
	msg_OID=$(echo $line | awk -F: '{print $2}' | awk '{$1=$1};1')
	printf "%s;" "$msg_OID"
done
printf "\n" 
