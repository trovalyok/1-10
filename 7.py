# Function as a Parameter

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def floor_divide(a, b):
    return a // b


def exponentiate(a, b):
    return a ** b


def modulo(a, b):
    return a % b


def apply_operation(operation, operand1, operand2):
    return operation(operand1, operand2)


print(apply_operation(exponentiate, -3, 3))


def test_apply_operation(func):
    x = 2
    y = 10
    result = ""

    if func(add, x, y) == 12:
        result += "test addition - success\n"
    else:
        result += "test addition - fail\n"

    if func(subtract, x, y) == -8:
        result += "test subtraction - success\n"
    else:
        result += "test subtraction - fail\n"

    if func(multiply, x, y) == 20:
        result += "test multiplication - success\n"
    else:
        result += "test multiplication - fail\n"

    if func(divide, x, y) == 0.2:
        result += "test division - success\n"
    else:
        result += "test division - fail\n"

    if func(floor_divide, x, y) == 0:
        result += "test floor division - success\n"
    else:
        result += "test floor division - fail\n"

    if func(exponentiate, x, y) == 1024:
        result += "test exponentiation - success\n"
    else:
        result += "test exponentiation - fail\n"

    if func(modulo, x, y) == 2:
        result += "test modulus - success"
    else:
        result += "test modulus - fail"

    return result


print(test_apply_operation(apply_operation))

# Function as a Return Value


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


m = input("Enter a multiplier (m): ")
while not is_float(m):
    print("That was not a numeric value.")
    m = input("Enter a multiplier (m): ")
m = float(m)

n = input("Enter a number (n): ")
while not is_float(n):
    print("That was not a numeric value.")
    n = input("Enter a number (n): ")
n = float(n)


def get_multiplier(x):
    def inner_function(y):
        return x * y
    return inner_function


multiplication_by_m = get_multiplier(m)
print(f"The result of multiplying n by m is {multiplication_by_m(n)}")

# Function as an Element of a List

operation_list = [add, subtract, multiply, divide, floor_divide,
                  exponentiate, modulo]

first_value = input("Enter a first numeric operand: ")
while not is_float(first_value):
    print("That was not a numeric value.")
    first_value = input("Enter a first numeric operand: ")
first_value = float(first_value)

second_value = input("Enter a second numeric operand: ")
while not is_float(second_value):
    print("That was not a numeric value.")
    second_value = input("Enter a second numeric operand: ")
second_value = float(second_value)

pair = [first_value, second_value]

for operation in operation_list:
    print(f'{pair[0]} {operation.__name__}\
 {pair[1]} = {operation(pair[0], pair[1])}')
