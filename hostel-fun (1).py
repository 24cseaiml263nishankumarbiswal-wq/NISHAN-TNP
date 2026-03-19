def allot_hostel(students, room_capacities):
    allotments = {}
    room_names = list(room_capacities.keys())
    room_index = 0
    
    for student in students:
        if room_index >= len(room_names):
            allotments[student] = "Waitlisted"
            continue
            
        current_room = room_names[room_index]
        allotments[student] = current_room
        room_capacities[current_room] -= 1
        
        if room_capacities[current_room] == 0:
            room_index += 1
            
    return allotments

applicants = ["Alice", "Bob", "Charlie", "David"]
hostel_inventory = {"A1": 2, "B1": 1}

output = allot_hostel(applicants, hostel_inventory)

for name, room in output.items():
    print(f"{name}: {room}")    