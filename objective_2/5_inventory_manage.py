'''python program that simulates a simple inventory manager using tuples;user should be able to
1.add item
2.remove item
3.update item quantity
4.view inventory
5.display items
6.manage multiple inventories
7.save and quit
'''
from datetime import datetime
import json

try:
    with open('tickets.json','r') as file:
        items = json.load(file)
except FileNotFoundError:
    items = []

#Function to add item
def add_item():
    id = input ("enter item id : ")
    name = input ("enter item name : ")
    quantity = input ("enter quantity : ")
    due_date = input ("enter yyyy-mm-dd")

    item= {
           "id" : id,
           "name" : name,
           "quantity" : quantity,
           "due_date" : due_date,
           "created" : datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
          }
    items.append(item)
    with open('tickets.json','w') as file:
        json.dump(items,file,indent=2)

#Function to view item
def view_item():
    identifier = input("enter item id :")

    for item in items:
        if item.get('id') == identifier:
            return item