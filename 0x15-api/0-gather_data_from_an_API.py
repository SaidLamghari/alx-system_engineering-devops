#!/usr/bin/python3
"""
Un script Python qui, en utilisant une API REST donnée,
récupère des informations sur
l'avancement de la liste de tâches d'un employé.
Autor: Said LAMGHARI
"""

import requests
import sys


if __name__ == "__main__":
    # URL de base pour l'API JSONPlaceholder
    base_url = "https://jsonplaceholder.typicode.com/"

    # Obtenir les informations sur
    # l'employé en utilisant l'ID d'employé fourni
    id_employe = sys.argv[1]
    infs_emply = requests.get(base_url + "users/{}".format(id_employe)).json()

    # Obtenir la liste de tâches à faire
    # pour l'employé en utilisant l'ID d'employé fourni
    todo_prms = {"userId": id_employe}
    todo_list = requests.get(base_url + "todos", todo_prms).json()

    # Filtrer les tâches terminées et les compter
    taches_terminees = []
    for tache in todo_list:
        if tache.get("completed"):
            taches_terminees.append(tache.get("title"))

    # Afficher le nom de l'employé
    # le nombre de tâches terminées
    print("Employee {} is done with tasks({}/{}):".format(
        infs_emply.get("name"), len(taches_terminees), len(todo_list)))

    # Afficher les tâches terminées une par une avec indentation
    for task_title in taches_terminees:
        print("\t", task_title)
