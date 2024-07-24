import hashlib as hash
import sqlite3

username = input("Enter your username: ")
password = input("Enter a password: ")

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

password_hash = hash.sha256(password.encode('utf-8')).hexdigest()

cursor.execute("INSERT INTO users ('username','password_hash') VALUES (?,?);", (username, password_hash))

connection.commit()
connection.close()