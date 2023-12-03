'''
python program for managing an address book that allows user to:
1.Add address
2.View address
  -view_address()
3.remove address
 -remove_address
 4.Quit
 -------------Main Menu------'''
import json
from utils import read_from_json,save_json_file


#Initialize an empty address book
contacts = read_from_json('contacts.json')
#Function to add contact
def add_contact():
    name=input("Enter the name of the contact:")
    address=input("Enter the address:")
    phone =input("Enter the phone number :")
    email=input("Enter the email address:")
    id = input("Enter id :")
    contact = {
              'id' : id,
              'name' : name,
              'address' : address,
              'email' : email,
              'phone' : phone,
             }
    contacts.append(contact)
    with open("contacts.json",'w') as phonebook:
        json.dump(contacts,phonebook,indent=2)
                   
    print(contact)



def contact_book():
    text = ("select the options below. \n1.Add contact . \n2.Remove contact .\n3.view contact . ")
    options = int(input(text))
    if options in [1,2,3]:
      if options == 1:
          add_contact()
      elif options == 2:
          remove_contact()
      elif options == 3:
          a = view_contact()
          print(a)
    else:
        print('Option out of range :)')

#Function to view contact
def view_contact():
      identifier = input("Enter id :")

      for contact in contacts:
          if contact.get('id')== identifier:
              return contact
        
#Function to remove contact:
def remove_contact():
    identifier = input("enter id :")

    for contact in contacts:
        if contact.get('id') == identifier:
            contacts.remove(contact)
            save_json_file(contacts,'contacts.json')

            print(f"contact successfully deleted.")

        else:
            print("invalid contact.")




contact_book()