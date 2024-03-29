#!/usr/bin/python3
"""
Gather data from an API
"""
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
        return user_data.get("name")
    else:
        print("Unable to fetch employee name")
        sys.exit(1)


def get_employee_todo_list(employee_id):
    """
    function to retrive the to do list
    """
    name = get_employee_name(employee_id)
    if not name:
        sys.exit(1)

    todo_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(todo_url)

    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo["completed"])

        print(
            f"Employee {name} is done with "
            f"tasks({completed_tasks}/{total_tasks}): "
        )
        for todo in todos:
            if todo["completed"]:
                print(f"\t{todo['title']}")
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
