#!/bin/bash

# snmpwalk -v3 -l authPriv -u $2 -a $3 -A $4 -x $5 -X $6 $1 $7
# $1 @IP
# $2 user
# $3 authProtocol
# $4 authKey
# $5 privProtocol
# $6 privKey
# $7 OID
snmpwalk -v3 -l authPriv -u $2 -a $3 -A $4 -x $5 -X $6 $1 $7 \
| while read line; do
	msg_OID=$(echo $line | awk -F: '{print $2}' | awk '{$1=$1};1')
	printf "%s;" "$msg_OID"
done
printf "\n" 
