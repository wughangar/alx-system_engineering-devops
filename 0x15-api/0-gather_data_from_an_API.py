#!/usr/bin/python3
"""
0. Gather data from an API
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    fucntion to get employee progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    print(f"Employee {user_data['name']} is done with
          tasks({completed_tasks}/{total_tasks}): ")
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid input")
