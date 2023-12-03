'''
python SQL module
'''

import sqlite3

#connecting sql to database 

connection = sqlite3.connect('fella.db')
cursor = connection.cursor()

#close connection when done
connection.close()

#creating a table
cursor.execute("create table if not exists(id:'int',username:'str' ,email:'str')")
connection.commit()

#inserting data

cursor.execute("INSERT INTO users(username, email) VALUES (?, ?), ('fella', 'fella@company.com)")
connection.commit()

#querying data
cursor.execute("SELECT * FROM users")
user = cursor.fetchall()

for user in user:
    print(user)

#updating data
cursor.execute("UPDATE isers SET email = ? WHERE username =?",('new_email@compamy.com,fella'))
connection.commit()

#deleting data
cursor.execute("DELETE FROM users WHERE username = ?",'fella')
connection.commit()