#!/usr/bin/python3
"""
Gather data from the JSONPlaceholder API.
This script accepts an employee ID as a parameter
and retrieves information about the
employee's progress on their TODO list from the JSONPlaceholder API.
"""

import requests
import sys


def get_employee_todo_list(employee_id):
    """
    function to retrive the to do list
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(todo_url)

    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])

        print(f"Employee EMPLOYEE_NAME is done with
              tasks({completed_tasks}/{total_tasks}): ")
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")
    else:
        print(f"Error: Unable to fetch data for employee {employee_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
