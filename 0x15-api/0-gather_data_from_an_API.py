#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    user = requests.get("{url}/users/{employee_id}").json()
    todos = requests.get(url + "/todos", params={"userId": employee_id}).json()

    completed_tasks = [data.get('title')
                       for data in todos if data.get('completed') is True]

    num_tasks = len(todos)
    done_tasks = len(completed_tasks)
    emp_name = user.get('name')

    print(f"Employee {emp_name} is done with tasks({done_tasks}/{num_tasks}):")
    [print(f"\t {title}") for title in completed_tasks]
