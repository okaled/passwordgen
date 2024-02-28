import sqlite3

def db_create():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                       id INTEGER PRIMARY KEY,
                       password TEXT
                    )''')
    connection.commit()
    connection.close()

def list_passwords():
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM passwords")
    passwords = cursor.fetchall()
    for password in passwords:
        print(password[0], password[1])
    connection.close()

db_create()
print('Your passwords are: ')
print()
list_passwords()

print()
input('Press Enter to close connection...')