#!/usr/bin/python3
'''Gets data in JSON format form a url and display it '''
import csv
import json
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 1:
        exit()

    users_info = requests.get("https://jsonplaceholder.typicode.com/users")
    users_info = users_info.json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = tasks.json()
    userid_str = sys.argv[1]
    user_id = int(sys.argv[1])

    username = ""
    for user in users_info:
        if user['id'] == user_id:
            username = user['username']
            break

    task_list = []
    filename = "{}.json".format(userid_str)
    with open(filename, 'w') as f:
        data_handler = csv.writer(f, delimiter=',')
        for task in tasks:
            if task['userId'] == user_id:
                info_dict = {"task": task['title'],
                             "completed": task['completed'],
                             "username": username}
                task_list.append(info_dict)
        json_dict = {userid_str: task_list}
        json.dump(json_dict, f)
