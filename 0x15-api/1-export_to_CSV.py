#!/usr/bin/python3
"""
Python script to export data in the CSV format.
Requirements:
    - Records all tasks that are owned by this employee
    - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    - File name must be: USER_ID.csv
"""
import csv
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(f"{url}/users/{user_id}").json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    username = user.get('username')
    file_name = user_id + ".csv"

    rows = []
    for data in todos:
        rows.append([user_id, username, data.get(
            'completed'), data.get('title')])

    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        [writer.writerow(row) for row in rows]
