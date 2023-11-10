# Utilisez une image de base avec Python
FROM python:3.8

# Installer le service SNMP
RUN apt-get update && apt-get install -y snmp

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le code de votre application dans le conteneur
COPY ./python /app

# Exposez le port 9000
EXPOSE 9000

# Installez les dépendances
RUN pip install -r requirements.txt

# Exécutez votre application au démarrage
CMD ["python", "app.py"]

