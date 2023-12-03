'''
sql
'''
import sqlite3
connection = sqlite3.connect('fella.sqlite')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL)")
connection.commit()

#inserting new user
cursor.execute("INSERT INTO users(username, email) VALUES(?, ?)",('fella_fine', 'fellafine@gmail.com'))
connection.commit()

#querrying data
cursor.execute("select * FROM users")
users = cursor.fetchall()

for user in users:
    print(user)

#updating user
cursor.execute("UPDATE users SET email = ? WHERE username = ?",('fella@gmail.com', 'fella_fine'))
connection.commit()