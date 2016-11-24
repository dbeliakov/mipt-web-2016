import json

def get_tasks(login):
    with open('tasks.json') as f:
        tasks = json.load(f)
    if not login in tasks:
        return []
    return tasks[login]

def add_task(login, text):
    with open('tasks.json') as f:
        tasks = json.load(f)
    if not login in tasks:
        tasks[login] = []
        task_id = 1
    else:
        if len(tasks[login]) == 0:
            task_id = 1
        else:
            task_id = tasks[login][-1]["id"] + 1
    tasks[login].append({"id": task_id, "text": text})
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
    return task_id

def remove_task(login, id):
    with open('tasks.json') as f:
        tasks = json.load(f)
    if not login in tasks:
        return
    for i, task in enumerate(tasks[login]):
        if task['id'] == id:
            del tasks[login][i]
            break
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
