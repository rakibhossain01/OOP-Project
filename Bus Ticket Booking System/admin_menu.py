from add import add_bus_to_system
from view_buses import view_buses

def admin_menu(system):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_bus_to_system(system)
        elif choice == '2':
            view_buses(system)
        elif choice == '3':
            print("Logging out of admin panel.")
            break
        else:
            print("Invalid choice. Please try again.")
