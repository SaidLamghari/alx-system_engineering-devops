#!/usr/bin/python3
"""
Un script Python qui, en utilisant une API REST donnée,
récupère des informations sur
l'avancement de la liste de tâches d'un employé
exporte les données au format CSV.
Autor: Said LAMGHARI
"""

import csv
import requests
import sys


def export_to_csv(user_id, username, tasks):
    """
    Exporte les tâches de l'employé vers un fichier CSV.
    :param user_id: ID de l'employé
    :param username: Nom de l'employé
    :param tasks: Liste des tâches
    """
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        cfiel = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=cfiel)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })


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

    # Exporter les tâches vers un fichier CSV
    export_to_csv(id_employe, infs_emply["name"], todo_list)

    print(f"Data exported to {id_employe}.csv successfully.")
