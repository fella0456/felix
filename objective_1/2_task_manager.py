'''
python program that simulates a to_do list using:
1.Add task
 -def add task
2.View task
 -def view task()
3.Mark task as complete
 -def mark as complete
4.Quit

'''
from datetime import  datetime
import json

from utils import read_from_json,save_json_file,search_item


tasks = read_from_json('tasks.json')

def add_task():
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    description = input("Enter description : ")

    task = {
        "id":id,
        "name":name,
        "description":description,
        "complete":False,
        "created_at":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        }
    
    tasks.append(task)
    save_json_file(list=tasks,filename='tasks.json')

def task_manager():
    text = ("select options below \n1.Add task. \n2.Mark as complete . \n3.View task .")
    options = int(input(text))
    if options == 1:
       add_task()
    elif options == 2:
        mark_complete()
    elif options == 3:
        view_item()

#Function to view task
def view_item():
    id = int(input("Enter task ID : "))
    return search_item(id,list=tasks)

def search_item(id,list):
    for task in list:
        if task.get('id') == id:
           return task
        else:
            return None


    
#Function to mark_as_complete
def mark_complete():
    id = int(input("enter task id : "))
    return search_item

def search_item(id):
    for task in tasks:
        if task.get('id')== id:
            complete = True
            save_json_file(tasks)

#Function to view task
def view_task():
    id = int(input("Enter task id :"))
    return search_item
def search_item(id):
    for task in tasks:
        if task.get('id') == id:
            print(task)
#Function to quit          
task_manager()