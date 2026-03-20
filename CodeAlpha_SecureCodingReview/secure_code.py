import hashlib
import getpass

# Stored hashed password (hash of "12345")
stored_password = hashlib.sha256("12345".encode()).hexdigest()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# Hash the entered password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username == "admin" and hashed_password == stored_password:
    print("Login successful!")
else:
    print("Login failed!")