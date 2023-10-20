# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:34:09 2023

@author: user
"""
from gevent.pywsgi import WSGIServer
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Utilisez une variable pour stocker les informations d'identification (à des fins de démonstration)
correct_username = "utilisateur"
correct_password = "motdepasse"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def check_login():
    username = request.form['username']
    password = request.form['password']

    if username == correct_username and password == correct_password:
        # Les informations d'identification sont correctes, redirigez vers la page protégée
        return redirect(url_for('page_protegee'))
    else:
        # Les informations d'identification sont incorrectes, affichez un message d'erreur
        return "Informations d'identification incorrectes. Veuillez réessayer."

@app.route('/page_protegee')
def page_protegee():
    return "Bienvenue sur la page protégée !"

if __name__ == '__main__':
    #app.run(port=8000, debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()


