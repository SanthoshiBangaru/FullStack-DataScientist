# 4. Movie Ticket Booking System
def available_seats(total_seats, booked):
    return [seat for seat in range(1, total_seats+1) if seat not in booked]

def book_seat(booked, seat):
    if seat in booked:
        return "Seat already booked!"
    booked.append(seat)
    return "Booking successful!"

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
        return "Cancellation successful!"
    return "Seat not booked!"

if __name__ == "__main__":
    total_seats = 10
    booked_seats = [2, 5, 7]

    print(book_seat(booked_seats, 3))
    print(cancel_seat(booked_seats, 5))
    print("Available seats:", available_seats(total_seats, booked_seats))