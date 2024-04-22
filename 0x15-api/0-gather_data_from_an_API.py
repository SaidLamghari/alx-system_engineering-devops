#!/usr/bin/python3
"""
Un script Python qui, en utilisant une API REST donnée,
récupère des informations sur
l'avancement de la liste de tâches d'un employé.
Auteur: Said LAMGHARI
"""

import requests
import sys


def get_todo_list_progress(employee_id):
    """
    Récupère et affiche des informations
    sur l'avancement de la liste
    de tâches d'un employé.

    Args:
        employee_id (int): L'ID de l'employé.

    Returns:
        None
    """
    base_lnk = 'https://jsonplaceholder.typicode.com'
    user_lnk = f'{base_lnk}/users/{employee_id}'
    todo_lnk = f'{base_lnk}/todos?userId={employee_id}'

    try:
        # Récupérer les informations sur l'utilisateur
        user_rspns = requests.get(user_lnk)
        user_dt = user_rspns.json()
        user_name = user_dt['name']

        # Récupérer la liste de tâches de l'employé
        todo_rspns = requests.get(todo_lnk)
        todo_dt = todo_rspns.json()

        # Calculer l'avancement
        total_tsks = len(todo_dt)
        completed_tsks = [
                task['title'] for task in todo_dt if task['completed']
                ]
        num_completed_tsks = len(completed_tsks)

        # Afficher les informations sur l'avancement
        print(f"L'employé {user_name} a terminé des tâches "
              f"({num_completed_tsks}/{total_tsks}):")
        for task in completed_tsks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        # Gérer les erreurs de requête
        print(f"Erreur : {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Valider les arguments en ligne de commande
        print("Utilisation : python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        # Valider l'ID de l'employé
        print("Erreur : L'ID de l'employé doit être un entier.")
        sys.exit(1)

    get_todo_list_progress(int(employee_id))
