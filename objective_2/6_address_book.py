''' 
create a python program thst simulates an address manager that allows user to:
1.create a new adress book
2.switch address book
3.delete address book
4.add contact
5.view contact
6.search contact
7.import contact
8.export contact
9.save and quit

'''
import json

try:
    with open ('phone.json','r') as file:
        contacts = json.load(file)
except FileNotFoundError:
        contacts = []
        
#Function to add contact
def add_contact():
    name = input("enter name : ")
    mobile = input("enter mobile : ")
    email = input("enter email : ")
    id = input("enter id : ")

    contact = {
               "name" :name,
               "mobile" : mobile,
               "email" : email,
               "id" : id
              }
    
    contacts.append(contact)

    with open ('phone.json','w') as file:
        json.dump(contacts,file,indent= 2)

#Function to view contact
def view_contact():
    identifier = int(input("enter id : "))

    for contact in contacts:
        if contact.get('id') == identifier:
           print(contact)
        
#Function to search contact
def search_contact():
    identifier =int(input("enter id : "))

    for contact in contacts:
        if contact['id'] == identifier:
            return contact

text = ("select options below. \n1.Add contact . \n2.View contact .\n3.Search contact . ")
options = int(input(text))
if options == 1:
    add_contact()
elif options == 2:
    view_contact()
elif options == 3:
    search_contact()

def address_manager():
    address_manager()
