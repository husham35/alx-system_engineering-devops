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

    number_of_task = len(todos)
    count_of_completed_task = len(completed_tasks)
    employee_name = user.get('name')

    print(f"Employee {employee_name} is done with tasks({count_of_completed_task}/{number_of_task}): ")
    [print(f"\t {title}") for title in completed_tasks]
