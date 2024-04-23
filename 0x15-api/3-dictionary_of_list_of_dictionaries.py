#!/usr/bin/python3
"""
Export data in the JSON format.
Autor: Said LAMGHARI
"""
# Import des modules nécessaires
import json
import requests
from sys import argv


# Définition de la fonction pour récupérer
# les informations d'un utilisateur
def fetch_user_info(user_id):
    """Fetch user information."""
    lnk = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    # Effectuer une requête GET pour
    # obtenir les informations de l'utilisateur
    response = requests.get(lnk)
    # Renvoyer les données JSON de la réponse
    # extraire le nom d'utilisateur
    return response.json().get('username')


# Définition de la fonction pour
# récupérer les tâches d'un utilisateur
def fetch_user_tasks(user_id):
    """Fetch user tsks."""
    lnk = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    # Effectuer une requête GET pour
    # obtenir les tâches de l'utilisateur
    response = requests.get(lnk)
    # Renvoyer les données JSON de la réponse
    return response.json()


# Définition de la fonction pour
# exporter les données au format JSON
def export_to_json():
    """Export data to JSON."""
    # Initialisation d'un dictionnaire
    # pour stocker toutes les données
    all_dta = {}
    # Boucle sur les IDs d'utilisateurs de 1 à 10
    for user_id in range(1, 11):  # Assuming user IDs are from 1 to 10
        # Récupérer le nom d'utilisateur
        username = fetch_user_info(user_id)
        # Récupérer les tâches de l'utilisateur
        tsks = fetch_user_tasks(user_id)
        # Ajouter les données de l'utilisateur au dictionnaire
        all_dta[str(user_id)] = [{
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
            } for task in tsks]
    # Écrire les données dans un fichier JSON
    with open('todo_all_employees.json', 'w') as jsn_fle:
        json.dump(all_dta, jsn_fle)


# Vérifier si le script est exécuté directement
if __name__ == "__main__":
    # Appeler la fonction d'exportation vers JSON
    export_to_json()
