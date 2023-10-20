#!/bin/bash

# $1 community
# $2 @IP
# $3 OID
snmpwalk -v2c -c $1 $2 $3 \
| while read line; do
	msg_OID=$(echo $line | awk -F: '{print $2}' | awk '{$1=$1};1')
	printf "%s;" "$msg_OID"
done
printf "\n" 
