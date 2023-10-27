import subprocess

### Parti SNMP v2c
comm = 'passprojet '
addr = '192.168.176.2 '

# Exécution du script bash
commande = './multi_SNMP_v2c.sh ' + comm + addr
process = subprocess.Popen(commande, shell=True, stdout=subprocess.PIPE)
sortie = process.stdout.read().decode()

# Utilisation de la sortie si nécessaire
#print(f"{sortie}")

# Diviser la chaîne en une liste en fonction des sauts de ligne
liste_lignes = sortie.split('\n')

### Partie SNMP v3
#./simple_SNMP_v3.sh 192.168.140.140 user1 SHA miracle2022 AES power2022 1.3.6.1.2.1.4.20.1.1
addrv3 = '192.168.140.140 '
userv3 = 'user1 '
authProtocol = 'SHA '
authKey = 'miracle2022 '
privProtocol = 'AES '
privKey = 'power2022 '

# Exécution du script bash
commande_v3 = './multi_SNMP_v3.sh ' + addrv3 + userv3 + authProtocol + authKey + privProtocol + privKey
process_v3 = subprocess.Popen(commande_v3, shell=True, stdout=subprocess.PIPE)
sortie_v3 = process_v3.stdout.read().decode()

# Diviser la chaîne en une liste en fonction des sauts de ligne
liste_lignes_v3 = sortie_v3.split('\n')

# Afficher chaque ligne séparément
for ligne in liste_lignes:
    print(ligne)

print('-----------------------------------')

for ligne in liste_lignes_v3:
    print(ligne)
