def book_ticket(system):
    bus_number = input("Enter Bus Number: ")
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone: ")
    system.book_ticket(bus_number, name, phone)
