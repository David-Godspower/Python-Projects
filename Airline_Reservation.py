import random
import string
import json
from datetime import datetime

print("A Program for Airline Reservation System.\n\n\n")

DATA_FILE = "airline_system.json"
Flight_Destinations = ["Lagos", "Kano","New York",]

# List to store all bookings
Booking_Details = []


def load_data():
    global Booking_Details
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            Booking_Details = data.get("Booking_Details", [])
    except (FileNotFoundError, json.JSONDecodeError):
        Booking_Details = []


# Save data to the file after every update
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump({"Booking_Details": Booking_Details}, file, indent=4)


# Function to generate a booking ID
def generate_booking_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # 6-character ID


# Function to generate a seat number
def generate_seat_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))  # 3-character seat number


# Book Flight function
def Book_a_Flight():
    while True:
        passenger_name = input("\nEnter Passenger Full Name:  ").title()

        if all(char.isalpha() or char.isspace() for char in passenger_name):
            if len(passenger_name) < 5:
                print("Name can't be less than five characters.")
            else:
                flight_destination = input("\nEnter Flight Destination:  ").title()
                if  flight_destination in Flight_Destinations:
                    date_of_travel = input("\nEnter Date of travel(dd-mm-yy):  ")
                    try:
                        # Modify the input_date to add "20" to the year if it's a 2-digit year
                        if len(date_of_travel.split('-')[2]) == 2:  # Check if the year is in 2 digits
                            date_of_travel = date_of_travel[:6] + "20" + date_of_travel[6:]  # Add "20" to the year

                        event_date = datetime.strptime(date_of_travel, "%d-%m-%Y").date()
                        today = datetime.today().date()

                        if event_date < today:
                            print("You cannot register for a past date.")
                        else:
                            print(f"Registration successful for {event_date.strftime('%d-%m-%Y')}")

                    except ValueError:
                        print("Invalid date format. Please use dd-mm-yy")
                        break
                else:
                    print("Invalid Destination")
                    break

                booking_id = generate_booking_id()
                seat_number = generate_seat_number()

                booking = {
                    "Booking ID": booking_id,
                    "Passenger Name": passenger_name,
                    "Flight Destination": flight_destination,
                    "Date of Travel": date_of_travel,
                    "Seat Number": seat_number
                }
                Booking_Details.append(booking)

                save_data()

                print("\nFlight successfully booked.")
                print("Booking Details:")
                for key, value in booking.items():
                    print(f"{key}:  {value}")
                break
        else:
            print("Invalid Name. Please use alphabetic characters and spaces only.")
            continue


# View Bookings Function
def View_Bookings():
    if Booking_Details:
        for bookings in Booking_Details:
            print("------------------------------")
            for key, value in bookings.items():
                print(f"{key}: {value}")
    else:
        print("No bookings available.")


# Cancel Bookings
def Cancel_Bookings():
    if not Booking_Details:
        print("No bookings at all.")
    else:
        booking_to_cancel = input("Enter the Booking ID to cancel: ").upper()
        for booking in Booking_Details:
            if booking["Booking ID"] == booking_to_cancel:
                Booking_Details.remove(booking)
                save_data()  # Save updated data
                print(f"Booking with ID {booking_to_cancel} has been cancelled.")
                break
        else:
            print("Booking ID not found.")



# Load existing data
load_data()

# Main Program Loop
while True:
    print("\n\nWelcome to the Airline Reservation System. \n\n")
    print("\t\t+++++MENU PAGE+++++\n \n 1) Book a Flight \n 2) View Bookings \n 3) Cancel Bookings \n 4) Exit \n")
    userinput = input("\tPlease Enter your choice:......    ").strip()
    if userinput == "1":
        Book_a_Flight()
    elif userinput == "2":
        View_Bookings()
    elif userinput == "3":
        Cancel_Bookings()
    elif userinput == "4":
        print("Goodbye! Thanks for making use of the system.")
        break
    else:
        print("Invalid Input")
