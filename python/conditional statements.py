base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"

# if statement to check the user eligibility
if age > 17:
    print("User is eligible to book a ticket")

# if statement to check if the age is greater or equal to  else print something else in case it isnt 
if age >= 21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for evening shows")


is_member = False
is_weekend = False
discount = 0

# chcks if theyre members and age to give discount
if is_member and age >= 21:
    discount = 3
    print("User qualifies for membership discount")
else:
    print("User does not qualify for membership discount")
print(f"Discount: {discount}")

# if showtime is evening (we use two equals sign)there are extra charges if not there are no charges
extra_charges = 0

if show_time == "Evening" or is_weekend:
    extra_charges = 2
    print("Extra charges will be applied")
else:
    print("No extra charges will be applied")
print(f"Extra charges: {extra_charges}")

# if age is that then the certain conditions are met
if age >= 21 or age >= 18 and (is_member or show_time != "Evening"):
    print("Ticket booking condition satisfied")
    service_charges = 0
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
         service_charges = 3
    
    else:
        service_charges = 1
    print("Service charges:", service_charges)
    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket: ",{final_price})
else:
    print("Ticket booking failed due to restrictions")









