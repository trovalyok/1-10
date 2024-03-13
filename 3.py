# All these expressions are true
print(10 > 5)
print(10 != 5)

print(42 == int("42"))
print(str(42) == "42")

print(3 < 4)
print(3 != 4)

# A text that contains a quote with double quotes
print('The quote "Never love anyone\
 who treats you like you\'re ordinary"\
 is often attributed to Oscar Wilde.')

# String palindrome detection
string1 = input('Enter a string:')
if string1 == string1[::-1]:
    print("The entered string is a palindrome")
else:
    print("The entered string isn't a palindrome")

# User's name and age
username = input('Enter your name:')
userage = input("Enter your age:")

string2 = "Your name is {0} and you are {1} years old"
print(string2.format(username, userage))

string2 = "Your name is {name} and you are {age} years old"
print(string2.format(name=username, age=userage))

string2 = f"Your name is {username} and you are {userage} years old"
print(string2)

# String formatting
str_1 = "Animals  "
print(str_1.lower())

str_2 = "  Badger"
print(str_2.upper())

str_3 = "   HoneyPot   "
print(str_3.lstrip())
print(str_3.rstrip())
print(str_3.strip())

string_1 = "Bear"
print(string_1.startswith('Be'))

string_2 = "bear"
print(string_2.startswith('Be'))

string_3 = "BEAR"
print(string_3.startswith('Be'))

string_4 = "bEar"
print(string_4.startswith('Be'))

formatted_string_2 = string_2.capitalize()
print(formatted_string_2.startswith('Be'))

formatted_string_3 = string_3.capitalize()
print(formatted_string_3.startswith('Be'))

formatted_string_4 = string_4.capitalize()
print(formatted_string_4.startswith('Be'))

# A secret message in the following text
text = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'
message = text[::-1].replace('X', '').replace('x', '')
print(message)
