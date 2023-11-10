# Projet Supervision SNMP

## Introduction

On se propose de développer un système de surveillance de matériel “réseau” à l’aide du protocole SNMP 

Les objectifs principaux de cette application sont de pouvoir : 

- Surveiller en ligne l’ensemble du matériel constituant le parc. Cette surveillance pourra avoir une représentation textuelle et graphique. 

- Sauvegarder (en fichier ou base de données) l’ensemble des données issues du matériel. 

- Gérer les défaillances matérielles (message d’erreur) en les reportant sur les interfaces “utilisateur” ainsi que dans les systèmes de “log”  

**Dans le cadre de ce développement, on souhaite tout d’abord se focaliser sur la surveillance du nombre d’octets traversant une interface réseau et afficher sous forme de graphe l’ensemble des données obtenues**

## Lancement

C'est un programme Python qui tourne sur un Docker


lancer le conteneur: <br>
`docker build -t snmp_app .` <br>
`docker run -p 9000:9000 snmp_app` <br>

Et connectez vous sur un navigateur:<br>
`http://127.0.0.1:9000`