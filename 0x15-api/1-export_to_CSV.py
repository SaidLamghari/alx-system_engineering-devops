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
    id_employe = sys.argv[1]
    infs_emply = requests.get(base_url + "users/{}".format(id_employe)).json()

    # Obtenir la liste de tâches à faire
    # pour l'employé en utilisant l'ID d'employé fourni
    todo_prms = {"userId": id_employe}
    todo_lst = requests.get(base_url + "todos", todo_prms).json()

    # Ouvrir un fichier CSV pour écrire les données
    with open("{}.csv".format(id_employe), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # En-tête du fichier CSV
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )
        # Écrire chaque tâche dans le fichier CSV
        for tsk in todo_lst:
            writer.writerow([
                id_employe,
                infs_emply.get("username"),
                str(tsk.get("completed")),
                tsk.get("title")
            ])
