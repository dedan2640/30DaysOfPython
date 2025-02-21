#LEVEL ONE

# 1. Create a set of IT companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 2. Find the length of the set it_companies
length_of_it_companies = len(it_companies)

# 3. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 4. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Tesla', 'Snapchat', 'Spotify'})

# 5. Remove one of the companies from the set it_companies
it_companies.remove('IBM')  # Removes 'IBM'

# 6. Difference between remove and discard
# `remove()` raises an error if the element is not found, while `discard()` does not raise an error.

# Try to remove an element that doesn't exist (for example 'NonExistentCompany')
try:
    it_companies.remove('NonExistentCompany')  # This will raise a KeyError if the company is not found
except KeyError:
    print("Element not found using remove()")

it_companies.discard('NonExistentCompany')  # This will not raise an error

# Output the results
length_of_it_companies, it_companies

#LEVEL TWO

# Step 1: Create sets A and B
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Step 2: Join A and B (Union)
union_A_B = A | B

# Step 3: Find A intersection B (Common elements)
intersection_A_B = A & B

# Step 4: Check if A is a subset of B
is_A_subset_of_B = A.issubset(B)

# Step 5: Check if A and B are disjoint sets
are_A_and_B_disjoint = A.isdisjoint(B)

# Step 6: Join A with B and B with A (Union is commutative, so it’s the same as Step 2)
union_A_B_reversed = B | A

# Step 7: Symmetric difference between A and B (Elements in A or B but not in both)
symmetric_difference_A_B = A ^ B

# Step 8: Delete the sets completely
del A
del B

# Output the results
union_A_B, intersection_A_B, is_A_subset_of_B, are_A_and_B_disjoint, union_A_B_reversed, symmetric_difference_A_B



