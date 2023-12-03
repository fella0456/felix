'''#designing a program that simulates simple inventory management that enables user to:
1.Add item
 -item = [
          {product id , name ,quantity},
          {product id , name ,quantity}
          ]
2.Remove item
3.View inventory
4.Quit
-----------Main menu----------
1.Add item
 -add_item
2.Remove item
 -remove_item
3.View item
 -view_item
5.quit
'''
from datetime import datetime
from utils import read_from_json, save_json_file


inventory = read_from_json()

#Function to add item
def add_item():
    id = input("Enter item id")
    name= input ("Enter item name")
    quantity = input("Enter quantity")
    description = input("Enter description")
    item = {
       "id":  id,
        "name"  :  name ,
        "quantity"  :  quantity,
        "description"  :  description,
         "created_at"  :  datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        }
    inventory.append(item)
    save_json_file(inventory)

    return item
                   

def inventory_manager():
    text = ("select options below.\n1.Add item . \n2.View item . \n3.Remove item . ") 
    options = int(input(text))
    if options ==  1:
        add_item()
    elif options == 2:
        view_item()
    elif options == 3:
        remove_item()

#Function to view item
def view_item():
    identifier = input("Enter ID or Name ")
    for item in inventory:
        if item.get('id') == identifier or item.get('name') == identifier:
          return item
        else:
            print("Item Not Found \n")

#Function to remove item
def remove_item():
    identifier = input("Enter ID or Name ")
    for item in inventory:
        if item.get('id') == identifier:
            inventory.remove(item)
            save_json_file(inventory)
            print(f"item succesfully deleted.")
        else:
            print("Item not found")

#Function to quit
inventory_manager()