import random
import numpy as np

# Integer input validation


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        print("That wasn't the integer value. Please enter an integer.")
        return False


def input_int():
    n = input("Enter an integer: ")
    while not is_integer(n):
        n = input("Enter an integer: ")
    return int(n)


print(f"The entered integer value is {input_int()}")

# A character at the index


def is_index(s, i):
    try:
        s[i]
        return True
    except IndexError:
        print("There is no element with this index in the given string.")
        return False


def input_str_and_int():
    string = input("Enter a string: ")
    index = input_int()
    while not is_index(string, index):
        string = input("Enter a string: ")
        index = input_int()
    return string[index]


print(f"string[integer] =  {input_str_and_int()}")

# Transaction

balance = 1000


def transaction(amount: int, _type: str) -> int:

    def deposit(amount):
        new_balance = balance + amount
        return new_balance

    def withdrawal(amount):
        new_balance = balance - amount
        return new_balance

    if _type == 'deposit':
        print(deposit(amount))
    elif _type == 'withdrawal':
        print(withdrawal(amount))
    else:
        print("This type isn't supported in this function. Use deposit or\
 withdrawal.")


transaction(100, 'deposit')
transaction(100, 'withdrawal')
transaction(100, 'abc')

# A dice roll
print(random.randint(1, 6))

# 1000 dice rolls
list_of_1000_dice_rolls = []

for i in range(1000):
    list_of_1000_dice_rolls.append(random.randint(1, 6))
    # print(list_of_1000_dice_rolls)

    c1 = list_of_1000_dice_rolls.count(1)
    c2 = list_of_1000_dice_rolls.count(2)
    c3 = list_of_1000_dice_rolls.count(3)
    c4 = list_of_1000_dice_rolls.count(4)
    c5 = list_of_1000_dice_rolls.count(5)
    c6 = list_of_1000_dice_rolls.count(6)

print(f"The number of 1: {c1}\nThe number of 2: {c2}\nThe number of 3:\
 {c3}\nThe number of 4: {c4}\nThe number of 5: {c5}\nThe number of 6: {c6}")

print(c1 + c2 + c3 + c4 + c5 + c6)

# An election for two candidates


def input_number_of_regions():
    n = input("Enter the number of regions: ")
    while not is_integer(n) or int(n) <= 0:
        print("That's an invalid value.")
        n = input("Enter the number of regions: ")
    return int(n)


def input_rating_for_1st(i):
    n = input(f"Enter a rating for 1st candidate in {i} region: ")
    while not is_integer(n) or int(n) < 0 or int(n) > 100:
        print("A rating must be an integer between 0 and 100 (percent)")
        n = input(f"Enter a rating for 1st candidate in {i} region: ")
    return int(n)


def receive_input():
    n = input_number_of_regions()
    r = []
    for i in range(n):
        r.append(input_rating_for_1st(i + 1))
    return (n, r)


voters = 10000  # in every region


def simulate_region_election(entered_data, region_number):
    # the number of successful trials out of the total number of trials
    v1_r = np.random.binomial(voters, entered_data[1][region_number] / 100)
    v2_r = voters - v1_r
    return (v1_r, v2_r)


def simulate_election(data):
    v1 = []
    v2 = []
    for i in range(data[0]):
        a = simulate_region_election(data, i)
        print(f"Region {i + 1}: {a[0]} votes for 1st candidate, {a[1]}\
 votes for 2nd candidate")
        v1.append(a[0])
        v2.append(a[1])
    return (v1, v2)


def calculate_result(v):
    sum_v = [sum(t) for t in v]
    m = max(sum_v)
    i = sum_v.index(m)
    p = 100 * m / sum(sum_v)
    return i, m, round(p, 1)


def announce_result(res):
    if res[0] == 0:
        w = "1st"
    else:
        w = "2nd"
    print(f"Result: {w} candidate won with {res[1]} votes and {res[2]}%\
 of all votes")


input_data = receive_input()
election_result = simulate_election(input_data)
result = calculate_result(election_result)
announce_result(result)
