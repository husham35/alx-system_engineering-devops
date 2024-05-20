#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{url}/users").json()
    todos = requests.get(url + "/todos").json()

    emp_dict = {}
    for user in users:
        arr = []
        user_id = user.get('id')
        for todo in todos:
            if user.get('id') == todo.get('userId'):
                arr.append({'task': todo.get('title'),
                            'completed': todo.get('completed'),
                            'username': user.get('username')})
        emp_dict[user_id] = arr

    file_name = "todo_all_employees.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(emp_dict, json_file)
