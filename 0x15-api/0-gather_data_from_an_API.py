#!/usr/bin/python3
"""
Un script Python qui, en utilisant une API REST donnée,
récupère des informations sur
l'avancement de la liste de tâches d'un employé.
Autor: Said LAMGHARI
"""

import requests
import sys


def gt_todo_prgrss(employee_id):
    """
    Récupère et affiche les informations
    sur l'avancement de la liste
    de tâches d'un employé.

    Args: employee_id (int): L'ID de l'employé.

    Returns: None
    """
    # URL de base pour l'API JSONPlaceholder
    base_lnk = "https://jsonplaceholder.typicode.com/"

    try:
        # Obtenir les informations sur l'employé
        # en utilisant l'ID d'employé fourni
        guser = requests.get(base_lnk + "users/{}".format(employee_id)).json()

        # Obtenir la liste de tâches de
        # l'employé en utilisant l'ID d'employé fourni
        params = {"userId": employee_id}
        todos = requests.get(base_lnk + "todos", params=params).json()

        # Filtrer les tâches terminées et les compter
        completed = [t.get("title") for t in todos if t.get("completed")]

        # Afficher le nom de l'employé et le nombre de tâches terminées
        print("Employee {} is done with tasks({}/{}):".format(
            guser.get("name"), len(completed), len(todos)))

        # Afficher les tâches terminées une par une avec indentation
        for complete in completed:
            print("\t{}".format(complete))

    except requests.exceptions.RequestException as e:
        # Gérer les erreurs de requête
        print(f"Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python3 nom_du_script.py <id_employé>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Erreur : L'ID de l'employé doit être un entier.")
        sys.exit(1)

    gt_todo_prgrss(int(employee_id))
