def add_bus_to_system(system):
    number = input("Enter Bus Number: ")
    route = input("Enter Route: ")
    seats = int(input("Enter Total Seats: "))
    system.add_bus(number, route, seats)
