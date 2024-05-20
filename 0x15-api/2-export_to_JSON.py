#!/usr/bin/python3
"""
Python script to export data in the JSON format.
Requirements:
    - Records all tasks that are owned by this employee
    - File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(f"{url}/users/{user_id}").json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    username = user.get('username')

    data = []
    dict = {}

    for todo in todos:
        data.append({'task': todo.get('title'),
                    'completed': todo.get('completed'), 'username': username})

    dict[user_id] = data

    file_name = user_id + ".json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json_text = json.dumps(dict)
        json_file.write(json_text)
