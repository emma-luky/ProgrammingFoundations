import re

"""
In Python, strings are immutable. This means that once a string object is created, its content cannot be changed.
Any operation that appears to modify a string, such as concatenation or replacement, actually results in the
creation of a new string object with the desired changes.
"""

value = input('Enter a number: ')
print(value + ' is my favorite number')

firstname = 'emma'
lastname = 'luk'
print(firstname.capitalize() + ' ' + lastname.capitalize())

"""
Methods
    .find()
    .index()
        - give you a reference to the first occurrence
    .rfind()
    .rindex()
        - give you a reference to the last occurrence
"""

"""
Regex
    /hello/
    \d - digits
    \w - word character
    . - any character
    + - 1 or more occurrences
    * - 0 or more
    ? - 0 or 1
    { num } - num of occurrences
"""
five_digit_zip = '94566'
nine_digit_zip = '98101-0003'
phone = '123-456-7890'
five_digit_regex = r'\d{5}'
print(re.search(five_digit_regex, five_digit_zip))
print(re.search(five_digit_regex, nine_digit_zip))
print(re.search(five_digit_regex, phone))