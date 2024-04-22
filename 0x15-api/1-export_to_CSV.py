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
    # Récupérer l'ID de l'utilisateur à partir
    # des arguments de la ligne de commande
    user_id = sys.argv[1]

    # Définir l'URL de base pour l'API JSON
    lnk = "https://jsonplaceholder.typicode.com/"

    # Récupérer les informations sur l'utilisateur depuis
    # l'API et convertir la réponse en objet JSON
    usr = requests.get(lnk + "users/{}".format(user_id)).json()

    # Extraire le nom d'utilisateur des données utilisateur
    usernme = usr.get("username")

    # Récupérer les éléments de la liste
    # de tâches associés à l'ID d'utilisateur
    # donné et convertir la réponse en objet JSON
    todos_in = requests.get(lnk + "todos", params={"userId": user_id}).json()

    # Écrire les éléments de la liste de tâches dans un fichier CSV
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Écrire l'en-tête CSV
        writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                )

        # Écrire chaque élément de la liste de tâches
        # en tant que ligne dans le fichier CSV
        for todo in todos_in:
            # Convertir le statut de complétion en
            # une représentation de chaîne (True ou False)
            cmptd_sts = str(todo.get("completed"))
            # Écrire les détails de chaque tâche en
            # tant que ligne dans le fichier CSV
            writer.writerow([user_id, usernme, cmptd_sts, todo.get("title")])
