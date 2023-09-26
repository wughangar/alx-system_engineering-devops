#!/usr/bin/python3
"""
Gather data from the JSONPlaceholder API.
This script accepts an employee ID as a parameter
and retrieves information about the
employee's progress on their TODO list from the JSONPlaceholder API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display an employee's TODO list progress
    Args:
        employee_id (int): The ID of the employee
        whose progress is to be retrieved.
    This function makes API requests to fetch
    information about the employee's TODO list,
    calculates the number of completed tasks, and prints the progress.

    Raises:
        requests.exceptions.RequestException: If the API request fails.

    Example:
        get_employee_todo_progress(2)
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
