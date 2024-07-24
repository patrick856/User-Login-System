import hashlib as hash
import sqlite3

credentials = []

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

for i, row in enumerate(rows):
    credentials.append({'username' : row[0], 'password' : row[1]})

def is_valid_credentials(username, password):
    stored_creds = None
    for cred in credentials:
        if cred['username'] == username:
            stored_creds = cred
    
    if stored_creds == None:
        return False

    return stored_creds['password'] == hash.sha256(password.encode('utf-8')).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

if is_valid_credentials(username, password):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

