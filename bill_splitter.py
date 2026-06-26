running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Calculate initial food total
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Calculate and add the tip
tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

# Split the bill among friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Round to two decimal places for currency
each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)