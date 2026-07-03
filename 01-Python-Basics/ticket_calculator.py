base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Membership Validation Check
is_member = False
is_weekend = False
discount = 0

if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Weekend & Timing Surcharges Check
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Core Booking Eligibility Engine with Complex Precedence Grouping
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Nested Seat Allocation Surcharge Matrix
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    # Final Accounting Aggregator
    final_price = service_charges + extra_charges + base_price - discount
    print('Final price of ticket:', final_price)
else:
    print('Ticket booking failed due to restrictions')