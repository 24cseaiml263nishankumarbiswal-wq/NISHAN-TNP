class ParkingLot:
    def __init__(self, spots):
        self.spots = spots
        self.occupied = {}

    def run(self):
        while True:
            print(f"\n--- Parking Lot (Available: {self.spots - len(self.occupied)}) ---")
            action = input("Type 'entry', 'exit', or 'quit': ").lower()
            
            if action == 'quit': break
            
            plate = input("Enter License Plate: ").upper()
            if action == 'entry':
                if len(self.occupied) < self.spots:
                    self.occupied[plate] = 10.0 # Standard fee
                    print(f"Vehicle {plate} parked.")
                else: print("Lot full!")
            elif action == 'exit':
                if plate in self.occupied:
                    self.occupied.pop(plate)
                    print(f"Vehicle {plate} removed. Fee paid: $10.00")
                else: print("Vehicle not found.")
ParkingLot(10).run()