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

def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    # Obtenir les informations sur l'employé en utilisant l'ID d'employé fourni
    response = requests.get(base_url + "users/{}".format(employee_id))
    if response.status_code != 200:
        raise Exception("Impossible de récupérer les informations sur l'employé.")
    
    employee_info = response.json()

    # Obtenir la liste de tâches à faire pour l'employé en utilisant l'ID d'employé fourni
    todo_params = {"userId": employee_id}
    response = requests.get(base_url + "todos", params=todo_params)
    if response.status_code != 200:
        raise Exception("Impossible de récupérer la liste des tâches de l'employé.")
    
    todo_list = response.json()

    return employee_info, todo_list

def write_to_csv(employee_id, employee_info, todo_list):
    with open("employee_{}.csv".format(employee_id), "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            writer.writerow([
                employee_id,
                employee_info.get("username"),
                str(task.get("completed")),
                task.get("title")
            ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        employee_info, todo_list = fetch_employee_data(employee_id)
        write_to_csv(employee_id, employee_info, todo_list)
        print("Les données ont été exportées avec succès.")
    except ValueError:
        print("L'ID de l'employé doit être un entier.")
    except Exception as e:
        print("Une erreur s'est produite:", str(e))
