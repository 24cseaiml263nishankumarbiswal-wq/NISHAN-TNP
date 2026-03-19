rooms = {
    "101": None,
    "102": None,
    "103": None,
    "104": None
}

while True:
    print("\n1. Allocate Room")
    print("2. Vacate Room")
    print("3. Room Info")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        for room in rooms:
            if rooms[room] is None:
                rooms[room] = name
                print(f"Room {room} allocated to {name}")
                break
        else:
            print("No rooms available")

    elif choice == "2":
        room = input("Enter room number to vacate: ")
        if room in rooms and rooms[room] is not None:
            rooms[room] = None
            print(f"Room {room} vacated successfully")
        else:
            print("Room is already vacant or invalid")

    elif choice == "3":
        print("\nRoom Status:")
        for room, name in rooms.items():
            status = f"Occupied by {name}" if name else "Vacant"
            print(f"Room {room}: {status}")

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice. Try again.")