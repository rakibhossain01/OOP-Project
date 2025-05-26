from admin_login import admin_login
from ticket import book_ticket
from view_buses import view_buses

def user_menu(system):
    while True:
        print("\n--- User Menu ---")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_login(system)
        elif choice == '2':
            book_ticket(system)
        elif choice == '3':
            view_buses(system)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
