#!/bin/bash

# En-tête du tableau
printf "%-20s %-15s %-15s %-15s\n" "Interface" "InOctets" "OutOctets" "Speed"

# Récupérer les informations SNMP
snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.2.2.1.1 \
| while read line; do
    interface=$(echo $line | awk -F: '{print $2}' | awk '{$1=$1};1')
    inOctets=$(snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.2.2.1.10.$interface | awk '{print $4}')
    outOctets=$(snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.2.2.1.16.$interface | awk '{print $4}')
    speed=$(snmpwalk -v3 -l authPriv -u user1 -a SHA -A miracle2022 -x AES -X power2022 192.168.140.140 1.3.6.1.2.1.2.2.1.5.$interface | awk '{print $4}')

    # Afficher les données dans le tableau
    printf "%-20s %-15s %-15s %-15s\n" "$interface" "$inOctets" "$outOctets" "$speed"
done

