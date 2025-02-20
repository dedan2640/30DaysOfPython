
#LEVEL ONE

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and brothers (imaginary siblings are fine)
sisters = ('Sarah', 'Margaret', 'Ubah')
brothers = ('Michael', 'Dedan')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
num_of_siblings = len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother
father_and_mother = ('James', 'Eve')
family_members = siblings + father_and_mother

# Output the results
empty_tuple, siblings, num_of_siblings, family_members



#LEVEL TWO

# Step 1: Unpack siblings and parents from family_members
siblings = family_members[:5]  # Assuming first 5 are siblings
parents = family_members[5:]   # Assuming last 2 are parents

# Step 2: Create fruits, vegetables, and animal products tuples
fruits = ('Apple', 'Banana', 'Orange', 'Grape')
vegetables = ('Carrot', 'Potato', 'Lettuce', 'Spinach')
animal_products = ('Milk', 'Cheese', 'Egg', 'Yogurt')

# Join the three tuples into a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Step 3: Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Step 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_item_tp = food_stuff_tp[len(food_stuff_tp) // 2]  # Middle item from tuple
middle_items_lt = food_stuff_lt[len(food_stuff_lt) // 2]  # Middle item from list

# Step 5: Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Step 6: Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Step 7: Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Step 8: Check if 'Estonia' and 'Iceland' are Nordic countries
is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries

# Output the results
siblings, parents, food_stuff_lt, middle_item_tp, middle_items_lt, first_three_items, last_three_items, is_estonia_nordic, is_iceland_nordic
