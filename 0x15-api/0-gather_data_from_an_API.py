#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO
  list progress in this exact format:
   ∆ First line: Employee EMPLOYEE_NAME is done with
     tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
     • EMPLOYEE_NAME: name of the employee
     • NUMBER_OF_DONE_TASKS: number of completed tasks
     • TOTAL_NUMBER_OF_TASKS: total number of tasks, which is
	   the sum of completed and non-completed tasks
   ∆ Second and N next lines display the title of completed tasks: TASK_TITLE
     (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import sys
import requests

if __name__ == '__main__':
  url = 'https://jsonplaceholder.typicode.com/'
  emp_id = sys.argv[1]

  user = requests.get(f"{url}/users/emp_id").json()
  todos = requests.get(url + "/todos", params={"userId": emp_id}).json()
  done = [data.get('title') for data in todos if data.get('completed') is True]
  tasks = len(todos)
  done_tasks = len(done)
  emp_name = user.get('name')

  print(f"Employee {emp_name} is done with tasks({done_tasks}/{tasks})")
  [print(f"\t {title}") for title in done]
