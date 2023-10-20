import subprocess

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

# Afficher chaque ligne séparément
for ligne in liste_lignes:
    print(ligne)
