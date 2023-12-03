''' simple to_do list that is able to
1.Add task
2.View task
3.Filter task
4.Set due date
5.View completed task
6.Task details
7.Save and Quit

'''
from datetime import datetime
import json
try:
    with open('manager.json','r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []
#function to add tasks
def add_task():
    id = input("enter id :")
    name = input("enter name :")
    description = input("enter description :")
    due_date = input("enter yyyy-mm-dd : ")

    task = {
         "id":id,
         "name":name,
         "description":description,
         "complete":False,
         "created":datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
         "due_date": due_date
        }
    tasks.append(task)
    
    with open('manager.json','w') as file:
        json.dump(tasks,file,indent = 2)

#Function to view task
def view_task():
    identifier = int(input("enter id"))
    
    for task in tasks:
        if identifier == id:
            return task
#Function to mark as complete
def mark_as_complete():
    identifier = input("enter id  : ")

    for task in tasks:
        if task.get('id') == identifier:
            task["complete"] = True
        with open('manager.json','w') as file:
            json.dump(tasks,file,indent = 2)

#Function to filter task
def filter_task(tasks):
    marked = []
    for task in tasks:
        if task['complete']==True:
            marked.append(task)
    print(marked)        


text = ("select options below.\n1.Add task . \n2.View task . \n3.Mark complete .\n4.Filter task. ")
options = int(input(text))
if options == 1:
    add_task()
elif options ==2:
    view_task()
elif options == 3:
    mark_as_complete()
elif options == 4:
    filter_task(tasks)

def task_manager():
    task_manager()