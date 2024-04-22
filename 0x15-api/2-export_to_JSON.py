#!/usr/bin/python3
"""
Un script Python qui, en utilisant une API REST donnée,
récupère des informations sur
l'avancement de la liste de tâches d'un employé
les exporte au format CSV.
Python script to export data in the JSON format
Autor: Said LAMGHARI
"""

import json
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
    id_employe = sys.argv[1]
    infs_emply = requests.get(base_url + "users/{}".format(id_employe)).json()

    # Obtenir la liste de tâches à faire
    # pour l'employé en utilisant l'ID d'employé fourni
    todo_prms = {"userId": id_employe}
    todo_lst = requests.get(base_url + "todos", todo_prms).json()

    # Créer un dictionnaire pour stocker les tâches
    tasks_dict = {id_employe: []}

    # Remplir le dictionnaire avec les données des tâches
    for tsk in todo_lst:
        task_info = {
            "task": tsk.get("title"),
            "completed": tsk.get("completed"),
            "username": infs_emply.get("username")
        }
        tasks_dict[id_employe].append(task_info)

    # Écrire le dictionnaire
    # dans un fichier JSON
    with open("{}.json".format(id_employe), "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)
