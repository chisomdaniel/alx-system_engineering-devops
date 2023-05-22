#!/usr/bin/python3
'''Gets data in JSON format form a url and display it '''
import csv
import json
import requests
import sys


if __name__ == "__main__":

    users_info = requests.get("https://jsonplaceholder.typicode.com/users")
    users_info = users_info.json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks.json()

    username = ""
    json_dict = {}
    for user in users_info:
        username = user['username']

        task_list = []
        for task in tasks:
            if task['userId'] == user['id']:
                info_dict = {"username": username,
                             "task": task['title'],
                             "completed": task['completed']}
                task_list.append(info_dict)
        json_dict.update({user['id']: task_list})

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json.dump(json_dict, f)
