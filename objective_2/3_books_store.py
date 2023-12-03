'''
python program that simulates a book store using:
1.Add book
2.View book
3.Filter books
4.Sort books
5.iterate through books
6.save and quit

'''
import json
try:
    with open('library.json','r')as file:
        books = json.load(file)
except FileNotFoundError:
    books = []

#Function to add book
def add_book():
    id = input ("enter id : ")
    name = input ("enter name : ")
    author = input("enter author : ")
    year = input("enter year : ")

    book ={
           "id" : id,
           "name" : name,
           "author" : author,
           "year" : year,
           "added" : False
          }
    books.append(book)

    with open('library.json','w') as file:
        json.dump(books,file, indent = 2)

#Function to view book
def view_book():
    identifier = input("enter id : ")

    for book in books:
        if book.get('id') == identifier:
            return book
    else:
        print("book not found")

#Function to mark as added
def mark_added():
    identifier = input("enter id : ")


    for book in books :
        if book.get('id') == identifier:
            book["added"] = True
            with open('library.json','w') as file:
                json.dump(books,file,indent=2)

#Function to filter books
def filter_book(books):
    marked = []

    for book in books:
        if book['added'] == True:
            marked.append(book)
        print(marked)


text = ("select options below.\n1.Add book . \n2.View book . \n3.Mark complete .\n4.Filter book. ")
options = int(input(text))
if options == 1:
    add_book()
elif options ==2:
    view_book()
    
elif options == 3:
    mark_added()
elif options == 4:
    filter_book(books)

#Function to save and quit




def books_library():
    books_library()