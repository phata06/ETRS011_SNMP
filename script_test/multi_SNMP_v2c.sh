#!/bin/bash

community=$1
addrIP=$2

# Liste des OIDs
#oid_ipaddr
oid_list[0]="1.3.6.1.2.1.4.20.1.1"
#oid_name
oid_list[1]="1.3.6.1.2.1.1.5"
#oid_contact
oid_list[2]="1.3.6.1.2.1.1.4"
#oid_descr
oid_list[3]="1.3.6.1.2.1.1.1"
#oid_location
oid_list[4]="1.3.6.1.2.1.1.6"
#oid_uptime
oid_list[5]="1.3.6.1.2.1.1.3"

# Boucle sur les OIDs
for oid in "${oid_list[@]}"
do
   ./simple_SNMP_v2c.sh $1 $2 $oid
#   snmpwalk -v2c -c $1 $2 $oid \
#	| while read line; do
#        	msg_OID=$(echo $line | awk -F': ' '{print $2}' | awk '{$1=$1};1')
#        	printf "%s;" "$msg_OID"
#	done
#   printf "\n"
done

