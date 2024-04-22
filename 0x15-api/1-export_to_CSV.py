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
    
    # Vérifier l'ID utilisateur et le nom d'utilisateur dans le fichier CSV
    user_ids_from_csv = set()
    usernames_from_csv = set()

    with open("{}.csv".format(id_employe), "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            user_ids_from_csv.add(row[0])
            usernames_from_csv.add(row[1])

    if id_employe in user_ids_from_csv and infs_emply.get("username") in usernames_from_csv:
        print("User ID and Username: OK")
    else:
        print("User ID: Incorrect / Username: Incorrect")
    
    # Vérifier le nombre de tâches dans le fichier CSV
    with open("{}.csv".format(id_employe), "r", newline="") as csvfile:
        task_count = sum(1 for row in csvfile) - 1  # Subtract header row
        if task_count == len(todo_lst):
            print("Number of tasks in CSV: OK")
        else:
            print("Number of tasks in CSV: Incorrect")

