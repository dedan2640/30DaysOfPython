# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6, 7]

# 3. Find the length of the list
length_of_list = len(my_list)

# 4. Get the first item, the middle item and the last item of the list
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]

# 5. Declare a list called mixed_data_types
mixed_data_types = ['John', 30, 5.9, 'Single', '1234 Elm Street']

# 6. Declare a list variable named it_companies and assign initial values
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
num_of_companies = len(it_companies)

# 9. Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'  # Changed Facebook to Meta

# 11. Add an IT company to it_companies
it_companies.append('Twitter')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Snapchat')

# 13. Change one of the it_companies names to uppercase (IBM excluded)
it_companies[1] = it_companies[1].upper()

# 14. Join the it_companies with a string '#;  '
companies_string = '#;  '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list
company_exists = 'Google' in it_companies

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
first_3_companies = it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
middle_company_slice = it_companies[len(it_companies) // 2]

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)

# 23. Remove the last IT company from the list
it_companies.pop()

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies


