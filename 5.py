# All these expressions are true
print(False == (not True))

print((True and False) == (True and False))

print(not (True and "A" == "B"))

# A solution for Wheat and chessboard problem
number_of_squares = 0
sum_of_grains = 0

while number_of_squares < 64:
    sum_of_grains = sum_of_grains + 2 ** number_of_squares
    number_of_squares += 1

print(sum_of_grains * 0.065 / (10 ** 6))

# A natural number from user input and all its divisors
number = input('Enter a natural number: ')

while number.isdigit() is False or int(number) == 0:
    print("That's not a natural number!")
    number = input('Enter a natural number:')

number = int(number)
divisors = []

for i in range(int(number ** 0.5)):
    if number % (i + 1) == 0:
        divisors.extend([i + 1, number // (i + 1)])

divisors.sort()
print('The divisors are', divisors)

# Triangle type identifier
a = input('Enter the length of the first side of the triangle: ')
while a.isdigit() is False or int(a) == 0:
    print("That's not a natural number!")
    a = input('Enter the length of the first side: ')
a = int(a)

b = input('Enter the length of the second side of the triangle: ')
while b.isdigit() is False or int(b) == 0:
    print("That's not a natural number!")
    b = input('Enter the length of the second side: ')
b = int(b)

c = input('Enter the length of the third side of the triangle: ')
while c.isdigit() is False or int(c) == 0:
    print("That's not a natural number!")
    c = input('Enter the length of the third side: ')
c = int(c)

if a + b <= c or a + c <= b or b + c <= a:
    print("There is no triangle with such sides")
elif a == b and b == c:
    print('A triangle is equilateral')
elif a == b or b == c or a == c:
    print('A triangle is isosceles')
else:
    print('A triangle is scalene')

# Longest consecutive symbol
string = input('Enter a string: ')

while not string:
    print('String is empty')
    string = input('Enter a string: ')

symbol = ""
max_count = 0
count = 1

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        count = count + 1
    else:
        if count > max_count:
            max_count = count
            symbol = string[i-1]
        count = 1
if count > max_count:
    symbol = string[-1]

print('First longest consecutive symbol: ' + symbol)

# The next day of a given date
year = input('Enter a year: ')
while year.isdigit() is False:
    print("That's not a natural number!")
    year = input('Enter a year: ')
year = int(year)

month = input('Enter a month: ')
while month.isdigit() is False or int(month) == 0 or int(month) > 12:
    print("That's not a valid value for the month!")
    month = input('Enter a month: ')
month = int(month)

day = input('Enter a day: ')
while True:
    if not day.isdigit() or int(day) == 0 or int(day) > 31:
        print("That's not a valid value for the day!")
    elif month in [4, 6, 9, 11] and int(day) > 30:
        print("This month has 30 days")
    elif month == 2 and year % 4 == 0 and int(day) > 29:
        print("This month has 29 days")
    elif month == 2 and year % 4 != 0 and int(day) > 28:
        print("This month has 28 days")
    else:
        break
    day = input('Enter a day: ')
day = int(day)

if day == 31 and month == 12:
    year += 1
    month = 1
    day = 1
elif day == 31 and month in [1, 3, 5, 7, 8, 10]:
    month += 1
    day = 1
elif day == 30 and month in [4, 6, 9, 11]:
    month += 1
    day = 1
elif day == 29 and month == 2 and year % 4 == 0:
    month += 1
    day = 1
elif day == 28 and month == 2 and year % 4 != 0:
    month += 1
    day = 1
else:
    day += 1

if day < 10:
    day = '0' + str(day)

if month < 10:
    month = '0' + str(month)

year = str(year)
if len(year) == 1:
    year = '000' + str(year)
elif len(year) == 2:
    year = '00' + str(year)
elif len(year) == 3:
    year = '0' + str(year)

print('The next date is [yyyy-mm-dd]: ' + year + '-' + month + '-' + day)
