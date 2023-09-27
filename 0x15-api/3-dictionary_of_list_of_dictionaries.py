#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
import sys


def get_employee_ids():
    """
    Function to get a list of all employee IDs
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users"

    response = requests.get(user_url)

    if response.status_code == 200:
        users_data = response.json()
        employee_ids = [user["id"] for user in users_data]
        return employee_ids
    else:
        print("Unable to fetch employee IDs")
        sys.exit(1)


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
        print(f"Unable to fetch employee name for ID {employee_id}")
        sys.exit(1)


def get_employee_todo_list(employee_id):
    """
    Function to retrieve the to-do list for a specific employee
    """
    username = get_employee_name(employee_id)
    if not username:
        sys.exit(1)

    todo_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(todo_url)

    if response.status_code == 200:
        todos = response.json()
        user_tasks = []

        for todo in todos:
            task_data = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"],
            }
            user_tasks.append(task_data)

        return user_tasks
    else:
        print(f"Error: Unable to fetch data for employee {employee_id}")
        return []


def export_all_employee_data():
    """
    Function to export data for all employees in JSON format
    """
    all_employee_data = {}

    employee_ids = get_employee_ids()

    for employee_id in employee_ids:
        tasks = get_employee_todo_list(employee_id)
        all_employee_data[employee_id] = tasks

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode="w") as json_file:
        json.dump(all_employee_data, json_file, indent=4)

    print(f"Data for all employees exported to {json_filename}")


if __name__ == "__main__":
    """
    Main function
    """
    base_url = "https://jsonplaceholder.typicode.com"
    export_all_employee_data()
