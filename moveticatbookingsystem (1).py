rows, cols = 5, 5
seats = [["O" for _ in range(cols)] for _ in range(rows)]

while True:
    print("\n  1 2 3 4 5")
    for i, r in enumerate(seats):
        print(f"{i+1} {' '.join(r)}")
    
    cmd = input("\nEnter row and col to book (e.g. '2 3') or 'quit': ")
    if cmd.lower() == 'quit': break
    
    try:
        r, c = map(int, cmd.split())
        if seats[r-1][c-1] == "O":
            seats[r-1][c-1] = "X"
            print("Seat Booked!")
        else: print("Seat already taken!")
    except: print("Invalid input. Use 'Row Col' format.")