import json

def read_from_json(filename='inventory.json'):
    try:
        with open(filename,'r') as file:
             inventory = json.load(file)
    except FileNotFoundError:
         inventory = []
    return inventory

def save_json_file(list,filename='inventory.json',mode='w'):
    with open(filename,mode) as file:
      json.dump(list,file,indent=2)

def search_item(id,list):
    for task in list:
        if task.get('id') == id:
           return task
        else:
            return None