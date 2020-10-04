# Do tuple slicing
month_tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Slice the 4th-7th element of tuple
month1 = month_tuple[4:8]
print("month_tuple[4:8]:",month1)

# Slice the first 4 element of tuple
month2 = month_tuple[:5]
print("month_tuple[:5]:",month2)

# Slice the 8th element and so on of tuple
month3 = month_tuple[8:]
print("month_tuple[8:]:",month3)

# Slice the 2nd-4th element of tuple from behind
month4 = month_tuple[-4:-1]
print("month_tuple[-4:-1]:",month4)

# Combine two lists/tuples or more
food_list = ['Gado-gado','Ayam goreng','Rendang']
beverage_list = ['Tea','Juice','Lemonade']
menu_list1 = food_list + beverage_list
menu_list2 = beverage_list + food_list
print("Menu:",menu_list1)
print("Menu:",menu_list2)

# Add the last element
food_list.append('Ketoprak')
print("List of food:",food_list)

# Remove all elements from a list
food_list.clear()
print("List of food:",food_list)

# Copy element of list
food_list1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
food_list2 = food_list1.copy()
food_list3 = food_list1
food_list2.append('Opor')
food_list3.append('Ketoprak')
print("List of food #1:",food_list1)
print("List of food #2:",food_list2)
print("List of food #3:",food_list3)

# Count the element frequency
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print("Count of 'Budi':",score_budi)
print("Count of 'Sud':",score_sud)

# Combine two list or more
food_list = ['Gado-gado', 'Ayam Goreng', 'Rendang']
beverage_list = ['Es Teh', 'Es Jeruk', 'Es Campur']
food_list.extend(beverage_list)
print("food_list.extend(beverage_list):",food_list)

# Get the index of an element
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
index_of_sud = list_score.index('Sud')
print("Index of the 1st 'Sud':",index_of_sud)

# Insert an element in a list
list_score = ['Budi','Sud','Budi','Budi','Sud']
print("Element of 3rd index:",list_score[3])
list_score.insert(3, 'Sud')
print("list_score:",list_score)
print("Element of 3rd index:",list_score[3])

# Remove an element on spesific location
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)

# Remove an element based on given value
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)

# Reverse the element
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print("Reversed menu:",list_menu)

# Sort the element
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print("Ascending:",list_menu) 
list_menu.sort(reverse=True)# Descending
print("Descending:",list_menu)

######################################################################

# Tuple manipulation with count() and index()
tuple_score = ('Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud')
score_budi = tuple_score.count('Budi')
score_sud = tuple_score.count('Sud')
print("Count of 'Budi':",score_budi)
print("Count of 'Sud':",score_sud)
the_first_sud = tuple_score.index('Sud')
print("First index found for 'Sud':",the_first_sud)

######################################################################

# Insert new data to the set
fruit_set = {'Orange','Apple','Grape'}
fruit_set.add('Melon')
print("Set #1:",fruit_set)
fruit_set.add('Apple')
print("Set #2:",fruit_set)

# Clear all elements of a set
fruit_set = {'Orange','Apple','Grape'}
fruit_set.clear()
print("fruit_set:",fruit_set)

# Copy all elements of a set
fruit_set1 = {'Orange','Apple','Grape'}
fruit_set2 = fruit_set1
fruit_set3 = fruit_set1.copy()
fruit_set2.add('Melon')
fruit_set3.add('Kiwi')
print("fruit_set1:",fruit_set1)
print("fruit_set2:",fruit_set2)
print("fruit_set3:",fruit_set3)

# Elements of parcel1 added by elements from parcel2
parcel1 = {'Grape','Apple','Orange'}
parcel2 = {'Apple','Kiwi','Melon'}
parcel1.update(parcel2)
print("parcel1:",parcel1)

# Remove an element randomly and with spesific value
parcel1 = {'Grape','Apple','Orange'}
parcel2 = parcel1.copy()
fruit = parcel1.pop()
print("Popped fruit:",fruit)
print("Parcel1 without popped fruit:",parcel1)
parcel2.remove('Apple')
print("Parcel2 without removed fruit:",parcel2)

# Unite two sets
parcel1 = {'Grape','Apple','Orange'}
parcel2 = {'Apple','Kiwi','Melon'}
parcel3 = parcel1.union(parcel2)
print("parcel3:",parcel3)

# Check whether a set is disjoint from another set
parcel1 = {'Grape','Apple','Orange'}
parcel2 = {'Kiwi','Melon','Banana'}
parcel3 = {'Apple','Srikaya','Watermelon'}
parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
print(parcel1_parcel2_disjoint)
parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
print(parcel1_parcel3_disjoint)

# Check whether a set is a subset or superset from another set
parcel_A = {'Grape', 'Apple'}
parcel_B = {'Durian','Watermelon','Apple'}
parcel_C = {'Grape', 'Kiwi', 'Apple', 'Orange', 'Melon'}
parcel_A_in_C = parcel_A.issubset(parcel_C)
parcel_B_in_C = parcel_B.issubset(parcel_C)
parcel_C_contains_A = parcel_C.issuperset(parcel_A)
parcel_C_contains_B = parcel_C.issuperset(parcel_B)
print("Is A a subset of C?",parcel_A_in_C)
print("Is B a subset of C?",parcel_B_in_C)
print("Is C a superset of A?",parcel_C_contains_A)
print("Is C a superset of B?",parcel_C_contains_B)

# Get the intersection and difference of sets
parcel_A = {'Grape', 'Kiwi', 'Apple', 'Orange', 'Melon'}
parcel_B = {'Apple', 'Orange', 'Watermelon', 'Durian', 'Tomato'}
parcel_C = parcel_A.intersection(parcel_B)
print("Intersection of A-B:",parcel_C)
parcel_C = parcel_A.difference(parcel_B)
print("Difference of A-B:",parcel_C)

# Get the symmetric difference
parcel_A = {'Grape', 'Apple', 'Orange', 'Melon'}
parcel_B = {'Apple','Orange','Watermelon','Lychee'}
parcel_C = parcel_A.symmetric_difference(parcel_B)
print(parcel_C)

######################################################################

# Get the list of key
employee = {
    'name' : 'Aksara',
    'id' : '1211011',
    'job' : 'Data Analyst'
}
list_key = list(employee.keys())
print(list_key)

# Get the values
value_dict = list(employee.values())
print(value_dict)

# Update dictionary
employee.update({'skillset':['Python', 'R']})
print(employee)

######################################################################

# Count the length of a list or tuple
tuple_menu = ('Gado-gado','Ayam Goreng','Rendang','Ketoprak')
count_menu = len(tuple_menu)
print("# of menu:",count_menu)

# Convert collection
fruit_list = ['Apple', 'Apple', 'Orange', 'Passion fruit', 'Orange', 'Passion fruit', 'Apple']
fruit_set = set(fruit_list)
print("Set of fruits:",fruit_set)
fruit_list = list(fruit_set)
print("List of fruits:",fruit_list)

######################################################################

# Accessing char of String based on spesific range, return the length of String
product_name = "Sepatu Niko"
product_name = product_name[:2] + "P" + product_name[3:9] + "K" + product_name[-1]
print(product_name)
print(product_name[:7])
print(product_name[7:])
print(len(product_name))

# Whitespace handling: strip()
greeting1 = ' Hello, good morning!   '
greeting1 = greeting1.strip()
print("strip():",greeting1)

# Whitespace handling: lstrip()
greeting2 = ' Hello, good morning!   '
greeting2 = greeting2.lstrip()
print("lstrip():",greeting2)

# Whitespace handling: rstrip()
greeting3 = ' Hello, good morning!   '
greeting3 = greeting3.rstrip()
print("rstrip():",greeting3)

# Caps handling
book1 = 'belajar bahasa Python'
book2 = 'Belajar Bahasa PYTHON.'
book3 = 'Belajar Bahasa PYTHON.'
print(book1.capitalize())
print(book2.lower())
print(book3.upper())

# Split String
words = "ani dan budi dan wati dan johan"
words1 = words.split("dan")
print("Split by 'dan':",words1)
words2 = words.split(" ")
print("Split by ' ':",words2)

# Join String
conjunction = " dan "
names = ["Ricky", "Peter", "Jordan"]
words = conjunction.join(names)
print(words)

# Replace String
words = "Malang apple is healthy, tasty, and is the freshest apple!"
words = words.replace("apple", "orange")
print(words)

# Find and count String
text = "Malang apple is the sweetest apple compared to other apples."
apple_freq = text.count("apple")
print(text.find("Apple"))
print(text.find("Malang"))
print("Frequency of 'apple':",apple_freq)

# Check if String starts with particular word
text = "Malang apple is the sweetest apple compared to other apples."
print(text.startswith("Malang"))
print(text.startswith("malang"))
print(text.endswith("apple"))
print(text.endswith("apples"))

######################################################################

# Read txt file: read()
files = open("hello.txt", "r")
content = files.read()
files.close()
print("read():",content)

# Read txt file: readline()
files = open("hello.txt", "r")
first_line = files.readline()
second_line = files.readline()
files.close()
print("readline():",first_line)
print(second_line)

# Read txt file: readlines()
files = open("hello.txt", "r")
all_lines = files.readlines()
files.close()
print("readlines():",all_lines)

# Read txt file: looping
files = open("hello.txt", "r")
for line in files:
    print(line)

# Write to hello.txt: mode w
files = open("hello.txt", "w")
files.write("Sekarang kita belajar menulis menggunakan Python\n")
files.write("Menulis konten file dengan mode w (write).")
files.close()
open_file = open("hello.txt", "r")
print(open_file.read())

# Write to hello.txt: mode a
files = open("hello.txt", "a")
files.writelines([
    "Sekarang kita belajar menulis menggunakan Python",
    "Menulis konten file dengan mode a (append)."
])
files.close()
open_file = open("hello.txt","r")
print(open_file.read())

################################################################
# Quiz

# Read file
house_file = open("harga_rumah.txt", "r")
data = house_file.readlines()
house_file.close()
print(data)

# Get the attribute key
house_key = data[0].replace("\n","").split(",")
print(house_key)

# Make a dictionary to store harga_rumah as key-value
house_price = []
for row in data[1:]:
    row_house = row.replace("\n","").split(",")
    dict_house_price = dict()
    for i in range(len(row_house)):
        dict_house_price[house_key[i]] = row_house[i]
    house_price.append(dict_house_price)
print(house_price)

# Return the list of values based on spesific attribute
def get_all_specified_attributes(list_of_dictionary, specified_key):
    list_attributes = []
    for data in list_of_dictionary:
        attr = data[specified_key]
        list_attributes.append(attr)
    return list_attributes

# Function to get the minimum value of an attribute
def min_value(list_attributes):
    min_attr =  9999
    for attr in list_attributes:
        if int(attr) < min_attr:
            min_attr = int(attr)
    return min_attr

# Function to get the maximum value of an attribute
def max_value(list_attributes):
    max_attr =  9999
    for attr in list_attributes:
        if int(attr) > max_attr:
            max_attr = int(attr)
    return max_attr

# Function to do value of attribute transformation
def transform_attr(attr, max_attr, min_attr):
    transform_val = (attr - min_attr) / (max_attr - min_attr)
    return transform_val

# Function to do data transformation
def data_transformation(list_of_dictionary, list_attributes_names):
    attr_info = {} #declare a set
    for attr_name in list_attributes_names:
        specified_attr = get_all_specified_attributes(list_of_dictionary, attr_name) #get the list of values of each attribute

        max_attr = max_value(specified_attr) #get max value of specified attribute
        min_attr = min_value(specified_attr) #get min value of specified attribute
        attr_info[attr_name] = {'max': max_attr, 'min': min_attr} #store max and min value of specified attribute
        
        data_idx = 0
        while(data_idx < len(list_of_dictionary)): #check if the data_idx is less than the length of data train
            list_of_dictionary[data_idx][attr_name] = transform_attr(int(list_of_dictionary[data_idx][attr_name]), max_attr, min_attr) #calling transformation function for each value in specified attributes. Start from: list_of_dictionary[0]['tanah']
            data_idx += 1 #increment for loop counter
    return list_of_dictionary, attr_info

# Function to transform data test
def transform_data(data, attr_info):
    for key_name in data.keys():
        data[key_name] = (data[key_name] - attr_info[key_name]['min']) / (attr_info[key_name]['max'] - attr_info[key_name]['min']) #transform data test for each value of attributes using the max-min value from data train transformation
    return data

# Function to convert a value to be an absolute number
def abs_value(value):
    if value < 0:
        return -value
    else:
        return value

# Function to predict the house price
def price_based_on_similarity(data, list_of_data):
    predicted_price = 0
    minimum_diff = 999    
    for data_point in list_of_data:
        #get the cumulative difference between data test and data train for each attribute
        diff = abs_value(data['tanah'] - data_point['tanah'])
        diff += abs_value(data['bangunan'] - data_point['bangunan'])
        diff += abs_value(data['jarak_ke_pusat'] - data_point['jarak_ke_pusat'])

        #get the minimum difference to predict the house price
        if diff < minimum_diff:
            predicted_price = data_point['harga']
            minimum_diff = diff
    
    return predicted_price

# Transform data train
house_price, attr_info = data_transformation(house_price, ['tanah','bangunan','jarak_ke_pusat'])

# Declare data test
data = {'tanah': 110, 'bangunan': 80, 'jarak_ke_pusat': 35}

# Transform data test
data = transform_data(data, attr_info)

# Calculate house price
price = price_based_on_similarity(data, house_price)
print("Predicted house price:",price)