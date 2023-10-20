#!/bin/bash

# En-tête du tableau
printf "%-10s %-20s %-20s\n" "Vlans" "Adresses MAC" "Adresses IP"

# Récupérer les informations SNMP
snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.3.1.1.1 \
| while read line; do
    interface=$(echo $line | awk -F: '{print $2}' | awk '{$1=$1};1')
    macaddr=$(snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.3.1.1.2.$interface | awk '{print $4, $5, $6, $7, $8, $9}')
    ipaddr=$(snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.3.1.1.3.$interface | awk '{print $4}')

    # Afficher les données dans le tableau
    printf "%-10s %-20s %-20s\n" "$interface" "$macaddr" "$ipaddr"
done

