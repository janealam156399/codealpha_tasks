# Vulnerable Login System

username = input("Enter username: ")
password = input("Enter password: ")

# Hardcoded credentials
if username == "admin" and password == "12345":
    print("Login successful!")
else:
    print("Login failed!")