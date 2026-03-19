rooms = [None] * 4  

while True:
    print("\nOptions:")
    print("1. Allocate Room")
    print("2. Vacate Room")
    print("3. Show Room Status")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        for i in range(len(rooms)):
            if rooms[i] is None:
                rooms[i] = name
                print(f"Room {i+1} allocated to {name}")
                break
        else:
            print("No rooms available")
    
    elif choice == "2":
        try:
            room_num = int(input("Enter room number to vacate (1-4): ")) - 1
            if 0 <= room_num < len(rooms) and rooms[room_num] is not None:
                rooms[room_num] = None
                print(f"Room {room_num+1} vacated")
            else:
                print("Room is already vacant or invalid")
        except ValueError:
            print("Invalid room number")
    
    elif choice == "3":
        print("\nRoom Status:")
        for i in range(len(rooms)):
            status = f"Occupied by {rooms[i]}" if rooms[i] else "Vacant"
            print(f"Room {i+1}: {status}")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Try again.")