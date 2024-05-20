#!/usr/bin/python3
"""
Python script to export data in the CSV format.
Requirements:
  - Records all tasks that are owned by this employee
  - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
  - File name must be: USER_ID.csv
"""
import sys
import requests
import csv

if __name__ == '__main__':
  url = 'https://jsonplaceholder.typicode.com/'
  emp_id = sys.argv[1]
  file_name = emp_id + '.csv'

  user = requests.get(f"{url}/users/emp_id").json()
  username = user.get('username')

  todos = requests.get(url + "/todos", params={"userId": emp_id}).json()

  rows = []

  for data in todos:
    rows.append([emp_id, username, data.get('completed'), data.get('title')])
  
  with open(file_name, "w", newline="") as csvfile:
    writer =  csv.writer(csvfile, delimiter=',',
                         quotechar='"', quoting=csv.QUOTE_ALL)
    [writer.writerow(row) for row in rows]
