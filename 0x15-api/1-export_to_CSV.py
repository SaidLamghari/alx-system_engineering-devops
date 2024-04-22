#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys

def get_todos(user_id):
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todos_url, params={"userId": user_id})
    todos = response.json()
    return todos

def get_username(user_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(user_url)
    user = response.json()
    return user["username"]

def export_to_csv(user_id, username, todos):
    filename = "{}.csv".format(user_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # En-têtes sans USER_ID
        for todo in todos:
            writer.writerow([username, todo["completed"], todo["title"]])  # Pas de USER_ID ici

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    todos = get_todos(user_id)
    username = get_username(user_id)

    export_to_csv(user_id, username, todos)
