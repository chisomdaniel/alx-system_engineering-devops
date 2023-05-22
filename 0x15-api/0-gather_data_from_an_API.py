#!/usr/bin/python3
'''Gets data in JSON format form a url and display it '''
import requests
import sys
import json


if __name__ == "__main__":

    if len(sys.argv) == 1:
        exit()

    users_info = requests.get("https://jsonplaceholder.typicode.com/users")
    users_info = users_info.json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks.json()
    user_id = int(sys.argv[1])

    name = ""
    for user in users_info:
        if user['id'] == user_id:
            name = user['name']
            break

    task_count = 0
    completed = 0
    task_list = []

    for task in tasks:
        if task['userId'] == user_id:
            task_count += 1
            if task['completed']:
                completed += 1
                task_list.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".format(name, completed,
                                                          task_count))
    for i in task_list:
        print("\t {}".format(i))
