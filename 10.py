import random

# Guessing the capital

capitals_of_countries = {
    'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin'  # ,
    # 'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
    # 'Switzerland': 'Bern', 'Austria': 'Vienna',
    # 'Belgium': 'Brussels',  'Sweden': 'Stockholm',
    # 'Norway': 'Oslo', 'Denmark': 'Copenhagen',
    # 'Finland': 'Helsinki', 'Poland': 'Warsaw',
    # 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens' """
}


def game(capitals):
    list_of_countries = list(capitals.keys())
    country = random.choice(list_of_countries)
    city = input(f"Guess the capital of {country} or quit by typing 'exit': ")
    points = 0
    lives = 2

    while list_of_countries:

        if city.lower() == 'exit' or lives == 0:
            print(f"Thanks for playing! Your final score is {points}.")
            break

        elif city.capitalize() == capitals[country]:
            points += 1
            print(f"You are right! Your current score is {points}.")

            if len(list_of_countries) > 1:
                # If the answer is correct, the country is not repeated.
                list_of_countries.remove(country)

                country = random.choice(list_of_countries)
                city = input(f"Guess the capital of {country} or quit\
 by typing 'exit': ")

            else:
                print("Congratulations! You've guessed all the capitals\
 correctly!")
                break

        else:
            print(f"Try again. Your current score is currently {points} and\
 you have {lives} more chances to make a mistake.")
            print(f"Hint: the capital's name begins with\
 {capitals[country][0:3-lives]}")
            lives -= 1
            city = input(f"Guess the capital of {country} or quit by typing\
 'exit': ")


game(capitals_of_countries)

# Convert a Roman numeral to a standard Arabic numeral


def roman_to_int(s: str) -> int:
    roman_arabic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
        'CD': 400, 'CM': 900
    }

    s.upper()
    sum = 0
    i = 0

    while i < len(s):
        if s[i:i+2] in roman_arabic.keys() and i+1 < len(s):
            sum += roman_arabic[s[i:i+2]]
            i += 2
        elif s[i] in roman_arabic.keys():
            sum += roman_arabic[s[i]]
            i += 1
        else:
            print("The value entered into the function isn't a Roman numeral.")
            break

    return sum


def test_roman_to_int():
    result1 = roman_to_int("III")
    assert result1 == 3

    result = roman_to_int("XLIX")
    assert result == 49

    result = roman_to_int("LVIII")
    assert result == 58

    result = roman_to_int("MCMLXXXIX")
    assert result == 1989

    result = roman_to_int("MCMXCIV")
    assert result == 1994


test_roman_to_int()

# Convert a standard Arabic numeral to a Roman numeral


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def int_to_roman(s: str) -> int:
    arabic_roman = {
        1: 'I', 5: 'V', 10: 'X', 50: 'L',
        100: 'C', 500: 'D', 1000: 'M',
        4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC',
        400: 'CD', 900: 'CM'
    }

    s = str(s)
    if is_integer(s) and len(s) < 5:
        roman = ""
        i = 0

        while i < len(s):
            if int(s[len(s)-(i+1):len(s)]) in arabic_roman.keys():
                roman = arabic_roman[int(s[len(s)-(i+1):len(s)])] + roman
                s = s[:len(s)-(i+1)] + '0' + s[len(s)-i:]
                i += 1

            elif int(s[len(s)-(i+1)]) > 5:
                for j in range(int(s[len(s)-(i+1)])-5):
                    s = s[:len(s)-(i+1)] + '1' + s[len(s)-i:]
                    roman = arabic_roman[int(s[len(s)-(i+1):len(s)])] + roman
                s = s[:len(s)-(i+1)] + '5' + s[len(s)-i:]

            else:
                for j in range(int(s[len(s)-(i+1)])):
                    s = s[:len(s)-(i+1)] + '1' + s[len(s)-i:]
                    roman = arabic_roman[int(s[len(s)-(i+1):len(s)])] + roman
                s = s[:len(s)-(i+1)] + '0' + s[len(s)-i:]
                i += 1

    else:
        print("The function converts if the argument is a four-digit integer.")

    return roman


def test_int_to_roman():
    result = int_to_roman(3)
    assert result == "III"

    result = int_to_roman(49)
    assert result == "XLIX"

    result = int_to_roman(58)
    assert result == "LVIII"

    result = int_to_roman(1873)
    assert result == "MDCCCLXXIII"

    result = int_to_roman(1989)
    assert result == "MCMLXXXIX"

    result = int_to_roman(1994)
    assert result == "MCMXCIV"

# The first element in the list that occurs the maximum number of times


def majority_element(nums: list) -> int:
    elements_quantity = {}
    for i in nums:
        elements_quantity[i] = nums.count(i)
    for k in elements_quantity.keys():
        if elements_quantity[k] == max(elements_quantity.values()):
            return k


def test_majority_element():
    result = majority_element([3, 2, 3])
    assert result == 3

    result = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result == 2

    result = majority_element([1, 2, 3, 4])
    assert result == 1


test_majority_element()

# Find missing subjects


def subjects_not_passed_by_all_students(student_exams):
    subject = {}
    result = set()

    for i in student_exams:
        if i[2] not in subject:
            subject[i[2]] = set()
        subject[i[2]].add(i[1])

    for i in subject:
        if max(subject[i]) < 60:
            result.add(i)

    return result


def test_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]

    assert subjects_not_passed_by_all_students(exams) == {"Science", "Math"}


test_subjects_not_passed_by_all_students()
