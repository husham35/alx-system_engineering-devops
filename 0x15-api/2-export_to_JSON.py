#!/usr/bin/python3
"""
Python script to export data in the JSON format.
Requirements:
  - Records all tasks that are owned by this employee
  - File name must be: USER_ID.json
"""
import sys
import requests
import json

if __name__ == '__main__':
  url = 'https://jsonplaceholder.typicode.com/'
  emp_id = sys.argv[1]
  file_name = emp_id + '.json'

  user = requests.get(f"{url}/users/{emp_id}").json()

  todos = requests.get(url + "/todos", params={"userId": emp_id}).json()
  emp_name = user.get('name')

  emp_dict = {}
  data = []

  for item in todos:
    data.append({'task': item.get('title'), 'completed': item.get('completed'),
                 'username': emp_name})
  
  emp_dict[emp_id] = data
  with open(file_name, "w", encoding='utf-8') as jsonfile:
    json_text_file =  json.dumps(emp_dict)
    jsonfile.write(json_text_file)
