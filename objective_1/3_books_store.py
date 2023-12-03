'''
Designing a simple book store that allows user to:
1.Add book
 -add_book
2.Remove book
 -remove_book
3.Display book
 -display_book
4.Search book
  search_book 
4.Quit
'''
from datetime import datetime
import json


from utils import read_from_json,save_json_file

books = read_from_json('books.json')

def add_book():
      """
      id : int
      name : str
      author : obj
      year : str
      """
      id = int(input("Enter id  : " ))
      name = input("Enter name  : "  )
      author = input("Enter author  : " )
      year = input("Enter year  : ")

      book = {
            "id":id,
            "name":name,
            "author":author,
            "year":year
        }
      books.append(book)
      save_json_file(list = books,filename = 'books.json')
  
      with open("books.json",'w') as library:
        json.dump(books,library,indent=2)
                   

#Function to view book:

def view_book():
     identifier = int(input("enter id : "))

     for book in books:
          if book.get('id') == identifier:
              return book
          else:
              return None

def book_store():
     text = input("select options below .\n1.Add book . \n2.View book .\n3.Remove book .")
     options = int(input(''))
     if options == 1:
          add_book()
     elif options == 2:
          view_book()
     elif options == 3:
          remove_book()
          
          

#Function to remove book

def remove_book():
     identifier = int(input("enter id : "))

     for book in books:
          if book.get('id') == identifier:
               books.remove(book)
               save_json_file(books,'books.json')
               print(f"book successfully removed.")
          else:
               print("book not found.")    

     
#Function to quit.

book_store()
