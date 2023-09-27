#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
import sys


def get_employee_name(employee_id):
    """
    Function to get employee name
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"

    response = requests.get(user_url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("username")
    else:
        print("Unable to fetch employee name")
        sys.exit(1)


def get_employee_todo_list(employee_id):
    """
    function to retrive the to do list
    """
    username = get_employee_name(employee_id)
    if not username:
        sys.exit(1)

    todo_url = f"{base_url}/todos?userId={employee_id}&name={name}"

    response = requests.get(todo_url)

    if response.status_code == 200:
        todos = response.json()
        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME",
                                 "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos:
                user_id = employee_id
                username = name
                task_completed_status = todo["completed"]
                task_title = todo["title"]
                csv_writer.writerow([user_id, username,
                                     task_completed_status, task_title])
        print(f"Data exported to {csv_filename}")

    else:
        print(f"Error: Unable to fetch data for employee {employee_id}")


if __name__ == "__main__":
    """
    main function
    """
    if len(sys.argv) != 2:
        print("Usage: python employee_todo.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    get_employee_todo_list(employee_id)
