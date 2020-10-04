# These are statements
print("Learning Python is fun!")
print("Hello, world!")

# Variables & literals
number1 = 5
number2 = 10
sentence1 = "Learning Python programming language"

# Operator
print(number1 + number2)

'''
This is multi line comments
We will make a simple program to calculate a total price
'''
init_price = 20000
discount = 2000
price_after_disc = init_price - discount
total = price_after_disc * 1.1
print("Total price after discount and 10% tax is ", total)

######################################################

# Create a list
list_example = [6, 'tujuh', 8, 9.0, 10]
print(list_example[0])
print(list_example[3])

# List is mutable
list_example[3] = 'empat'
print(list_example[3])

# Tuple is immutable
tuple_example = ('Juni', 'Juli', 'Agustus', 'September')
#tuple_example[0] = 'Desember'
print(tuple_example[0])

# The difference between set and sequence
set1 = {'Theo', 'Annette', 'Mel', 'Handy', 'Mel'}
print("This is set: ", set1)
list1 = ['Theo', 'Annette', 'Mel', 'Handy', 'Mel']
print("This is list: ", list1)

# This is a dictionary
person = {'name': 'Theo Lau', 'job': 'Data Analyst'}
print(person['name'])
print(person['job'])

######################################################

# Make dictionaries for each product
shoe = {"name":"Niko", "price":150000, "disc":30000}
cloth = {"name":"Unikloh", "price":80000, "disc":8000}
pant = {"name":"Lepis", "price":200000, "disc":60000}

# Calculate price with discount for each product
shoe_subtotal = shoe["price"] - shoe["disc"]
cloth_subtotal = cloth["price"] - cloth["disc"]
pant_subtotal = pant["price"] - pant["disc"]

# Calculate subtotal after discount
total_price = shoe_subtotal + cloth_subtotal + pant_subtotal

# Calculate price with tax
total_tax = total_price * 0.1

# Display the overall total
print("The total price after discount and tax is ", total_price + total_tax)

######################################################

# Implement operator priority in calculating total price
init_price = 150000
discount = 0.3
tax = 0.1
total_price = (1 - discount) * init_price
total_price += total_price * tax
print("The total price is", total_price)

number = (3 + 2) ** 2 + (4 + 4) / 2 % 4
print(number)

######################################################

# if-elif-else statement
the_time = 13
if the_time >= 5 and the_time < 12:
    the_greeting = "Good morning!"
elif the_time >= 12 and the_time < 17:
    the_greeting = "Good afternoon!"
else:
    the_greeting = "Good evening!"
print(the_greeting)

# Case study
the_time = 17
user = "Mr. Yoyo"
warehousing = {'cost_per_day': 1000000, 'num_of_days': 15} 
cleansing = {'cost_per_day': 1500000, 'num_of_days': 10}
integration = {'cost_per_day': 2000000, 'num_of_days': 15} 
transform = {'cost_per_day': 2500000, 'num_of_days': 10}

sub_warehousing = warehousing['cost_per_day'] * warehousing['num_of_days'] 
sub_cleansing = cleansing['cost_per_day'] * cleansing['num_of_days'] 
sub_integration = integration['cost_per_day'] * integration['num_of_days'] 
sub_transform = transform['cost_per_day'] * transform['num_of_days']
total = sub_warehousing + sub_cleansing + sub_integration + sub_transform

if the_time >= 17:
    the_greeting = "Good evening,"
elif the_time >= 12:
    the_greeting = "Good afternoon,"
else:
    the_greeting = "Good morning,"
print("Bill of payment of:",user,"\n",the_greeting,user,"\n","This is your bill of payment:",total)

######################################################

transport_cost = 1500000
num_of_days = 31
vehicle_number = [8993, 2198, 2501, 2735, 3772, 4837, 9152]

# Check whether the vehicle_number is odd or even and count of each
even_vehicle = 0 
odd_vehicle = 0
for vehicle_id in vehicle_number:
    if vehicle_id % 2 == 0:
        even_vehicle += 1
    else:
        odd_vehicle += 1

# Calculate the total_cost
i = 1
total_cost = 0
while i <= num_of_days:
    if i % 2 == 0:
        total_cost += (even_vehicle * transport_cost) 
    else:
        total_cost += (odd_vehicle * transport_cost) 
    i += 1

print("Total cost for a month:",total_cost)