# Utiliser une image de base
FROM debian:buster-slim

# Installer le service SNMP
RUN apt-get update && apt-get install -y snmpd

# Copier la configuration SNMP
COPY snmpd.conf /etc/snmp/snmpd.conf

# Exposer le port SNMP
EXPOSE 161/udp

# Commande à exécuter à chaque démarrage du conteneur
CMD ["snmpd", "-f", "-Lo"]