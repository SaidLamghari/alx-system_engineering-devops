#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


def export_to_csv(user_id, username, tasks):
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([user_id, username, task["completed"], task["title"]])


if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and
    #   convert the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated with the
    #   given user ID and convert the response to a JSON object
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Export the to-do list items to a CSV file
    export_to_csv(user_id, username, todos)
