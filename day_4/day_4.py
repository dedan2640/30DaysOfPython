# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' into a single string 'Thirty Days Of Python'
string1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(string1)

# 2. Concatenate the string 'Coding', 'For', 'All' into a single string 'Coding For All'
string2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(string2)

# 3. Declare a variable named company and assign it to "Coding For All"
company = "Coding For All"
print(company)

# 4. Print the length of the company string using len() method
print(len(company))

# 5. Change all the characters to uppercase letters using upper() method
print(company.upper())

# 6. Change all the characters to lowercase letters using lower() method
print(company.lower())

# 7. Use capitalize(), title(), swapcase() methods to format the string 'Coding For All'
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 8. Cut (slice) out the first word of 'Coding For All'
first_word = company.split()[0]
print(first_word)

# 9. Check if 'Coding For All' string contains the word 'Coding' using index() or find()
print(company.find('Coding'))
print(company.index('Coding'))

# 10. Replace the word 'coding' in 'Coding For All' to 'Python'
print(company.replace('Coding', 'Python'))

# 11. Change 'Python for Everyone' to 'Python for All' using replace() method
sentence = 'Python for Everyone'
print(sentence.replace('Everyone', 'All'))

# 12. Split the string 'Coding For All' using space as the separator (split())
words = company.split()
print(words)

# 13. Split the string 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' at the comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(', ')
print(split_companies)

# 14. What is the character at index 0 in the string 'Coding For All'
print(company[0])

# 15. What is the last index of the string 'Coding For All'
print(len(company) - 1)

# 16. What character is at index 10 in 'Coding For All' string
print(company[10])

# 17. Create an acronym or abbreviation for the name 'Python For Everyone'
acronym = ''.join([word[0].upper() for word in "Python For Everyone".split()])
print(acronym)

# 18. Create an acronym or abbreviation for the name 'Coding For All'
acronym = ''.join([word[0].upper() for word in "Coding For All".split()])
print(acronym)

# 19. Use index() to determine the position of the first occurrence of 'C' in 'Coding For All'
print(company.index('C'))

# 20. Use index() to determine the position of the first occurrence of 'F' in 'Coding For All'
print(company.index('F'))

# 21. Use rfind() to determine the position of the last occurrence of 'l' in 'Coding For All'
print(company.rfind('l'))

# 22. Use index() or find() to find the position of the first occurrence of the word 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 23. Use rindex() to find the position of the last occurrence of the word 'because'
print(sentence.rfind('because'))

# 24. Slice out the phrase 'because because because' in the sentence
print(sentence[sentence.find('because'):sentence.rfind('because') + len('because')])

# 25. Find the position of the first occurrence of the word 'because' in the sentence
print(sentence.find('because'))

# 26. Slice out the phrase 'because because because' in the sentence
print(sentence[sentence.find('because'):sentence.rfind('because') + len('because')])

# 27. Check if 'Coding For All' starts with the substring 'Coding'
print(company.startswith('Coding'))

# 28. Check if 'Coding For All' ends with the substring 'coding'
print(company.endswith('coding'))

# 29. Remove the left and right trailing spaces in '   Coding For All      '
print('   Coding For All      '.strip())

# 30. Which one of the following variables returns True when we use the method isidentifier()?
print("30DaysOfPython".isidentifier())  # False, it starts with a number
print("thirty_days_of_python".isidentifier())  # True, it is a valid identifier

# 31. Join the list of Python libraries with a hash ('#') with space string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# 32. Use a new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

# 33. Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 34. Use the string formatting method to display the area of a circle with radius 10
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 35. Make the following calculations using string formatting
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # To display 2 decimal places
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
