#This code is for calulating the flight module details

#List of datas presented 
flight_no = "AI203"
base_fare = "4500.75"
tax_percent = "5"
seat_numbers = "12A,12B,14C,15D"
is_international = "True"

#Task 1 - to convert the data in proper numeric type

base_fare = float(base_fare)

#print(type(base_fare))

tax_percent = float(tax_percent)

#Task 1a - to calculate the final fare for single passenger

final_fare = base_fare + (base_fare * ((tax_percent)/100))

print(f"The final fare for single passenger is Rs {final_fare}")

#Task 2 - to convert the seat values into a list

lst_seat_no = seat_numbers.split(",")

print(lst_seat_no)

# Task 3 - to convert the list into set

seat_no = set(lst_seat_no)

print(seat_no)

#Task 4 - to convert the is_international value

is_international = bool(is_international)

print(type(is_international))


#Task 5 - creating a dictionary


flight_summary ={}

flight_summary["flight_no"] = "AI203"
flight_summary["final_fare"] = int(final_fare)
flight_summary["seat_numbers"] = tuple(lst_seat_no)

print(type(flight_summary))

print(flight_summary)

