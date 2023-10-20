# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:12:01 2023

@author: user
"""

from flask import Flask, render_template, request, redirect, url_for,session
from equipment_manager import EquipmentManager 

app = Flask(__name__)
manager = EquipmentManager('equipement.json')

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    equipment_list = manager.get_equipment_list()
    return render_template('index.html', equipment_list=equipment_list)

@app.route('/add_equipment', methods=['POST'])
def add_equipment():
    nom = request.form['nom']
    adresse_ip = request.form['adresse_ip']
    port = request.form['port']
    communaute = request.form['communaute']
    oids = request.form['oids']
    manager.add_equipment(nom, adresse_ip, port, communaute, oids)
    return redirect(url_for('index'))

@app.route('/remove_equipment', methods=['POST'])
def remove_equipment():
    nom = request.form['nom']
    adresse_ip = request.form['adresse_ip']
    manager.remove_equipment(nom, adresse_ip)
    return redirect(url_for('index'))

#----------------------- Partie 2 ------------------
app.secret_key = 'user'  # Clé secrète pour la gestion des sessions

# Une structure de données (à des fins de démonstration) pour stocker les informations d'identification

users = {
    'ndiaye': '1234',
    'nicolas': '5678'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Informations d'identification incorrectes. Veuillez réessayer."

    return render_template('auth.html')





@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

#----------------------------- Partie 3 --------------
@app.route('/get_equipment_info', methods=['POST'])
def get_equipment_info():
    selected_ip = request.form['selected_equipment']
    selected_equipment = None
    
    # Recherchez l'équipement en fonction de l'adresse IP sélectionnée
    for equipment in manager.get_equipment_list():
        if equipment['AdresseIP'] == selected_ip:
            selected_equipment = equipment
            break
    
    if selected_equipment:
        # Affichez les informations de l'équipement (par exemple, dans un modèle séparé)
        return render_template('equipment_info.html', equipment=selected_equipment)
    else:
        return "Équipement introuvable."



#@app.route('/')
#def index():
#    if not session.get('logged_in'):
#        return redirect(url_for('login'))
#    # Votre page "index.html" pour gérer les équipements
#    return render_template('index.html')






    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)


