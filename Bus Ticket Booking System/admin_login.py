from admin import Admin
from admin_menu import admin_menu

def admin_login(system):
    admin = Admin("admin", "1234")
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    if admin.login(username, password):
        print("Login successful!")
        admin_menu(system)
    else:
        print("Invalid credentials.")
