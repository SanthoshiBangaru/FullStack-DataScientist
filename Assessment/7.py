# 7. Taxi Fare Calculation
def calculate_fare(distance):
    base_fare = 50
    per_km = 10
    return base_fare + (per_km * distance)

def calculate_total(trips):
    total = 0
    for i, trip in enumerate(trips, 1):
        fare = calculate_fare(trip)
        total += fare
        print(f"Trip {i}: ${fare}")
    print("Total Fare: $" + str(total))

if __name__ == "__main__":
    trips = [5, 10, 3]
    calculate_total(trips)