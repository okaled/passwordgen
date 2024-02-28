import random
import string
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

def pass_insert(password):
    connection = sqlite3.connect('passwords.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
    connection.commit()
    connection.close()

def generate_password(length):
    caracteres = string.ascii_letters + string.digits
    password = ''.join(random.choice(caracteres) for i in range(length))
    pass_insert(password)
    return password

def main():
    length = int(input("Type the desired password length: "))
    generated_password = generate_password(length)
    print("Your generated password is:", generated_password)

if __name__ == "__main__":
    db_create()
    main()

input('Press Enter to close connection...')