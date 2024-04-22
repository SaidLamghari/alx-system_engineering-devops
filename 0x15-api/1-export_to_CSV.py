#!/usr/bin/python3
"""
Un script Python qui, en utilisant une API REST donnée,
récupère des informations sur
l'avancement de la liste de tâches d'un employé
les exporte au format CSV.
Autor: Said LAMGHARI
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    # URL de base pour l'API JSONPlaceholder
    base_url = "https://jsonplaceholder.typicode.com/"

    # Obtenir les informations sur
    # l'employé en utilisant l'ID d'employé fourni
    user_id = sys.argv[1]
    user_info = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user_info.get("username")

    # Obtenir la liste de tâches à faire
    # pour l'employé en utilisant l'ID d'employé fourni
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    # Écrire les données dans un fichier CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])

