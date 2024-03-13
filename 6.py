# All the prime numbers between a and b (inclusive)


def find_primes():
    primes = []

    a = input('Enter a first natural number: ')
    while not a.isdigit() or int(a) == 0:
        print("That's not a natural number!")
        a = input('Enter a first natural number: ')
    a = int(a)

    b = input('Enter a second natural number: ')
    while not b.isdigit() or int(b) == 0:
        print("That's not a natural number!")
        b = input('Enter a first natural number: ')
    b = int(b)

    if a > b:
        temp = a
        a = b
        b = temp

    for value in range(a, b + 1):
        divisors = []
        for i in range(int(value ** 0.5)):
            if value % (i + 1) == 0 and i != 0:
                divisors.append(i)
        if not divisors and value != 1:
            primes.append(value)

    return a, b, primes


result1 = find_primes()
print(f'Between {result1[0]} and {result1[1]} (inclusive) are the following \
prime numbers: {result1[2]}')

# Whether or not all characters in a string are unique


def unique_characters():
    s = input('Enter a string: ')
    for i in s:
        if s.count(i) != 1:
            return False
    return True


print(f'All the characters in the entered string are unique - \
{unique_characters()}')

# Calculating the Fibonacci series


def fibonacci():
    n = input('Enter a number of iterations: ')
    while not n.isdigit() or int(n) == 0:
        print("That's not a natural number!")
        n = input('Enter a number of iterations: ')
    n = int(n)

    a0 = 0
    a1 = 1
    sum = 1
    for i in range(1, n):
        sum = a1 + a0
        a0 = a1
        a1 = sum

    return n, sum


result2 = fibonacci()
print(f'{result2[0]} element of the Fibonacci sequence is {result2[1]}')

# swapcase()


def swapcase(input_string: str) -> str:

    for i in range(len(input_string)):
        if input_string[i].islower():
            input_string = (input_string[:i] + input_string[i].upper() +
                            input_string[i + 1:])
        else:
            input_string = (input_string[:i] + input_string[i].lower() +
                            input_string[i + 1:])

    return input_string


print(swapcase('HelLo!'))

# Calculating the performance of a deposit in a bank account


def simple_interest(initial_amount, interest_rate: float, years):
    s = initial_amount

    for i in range(0, years):
        s = s + s * interest_rate

    return round(s, 2)


print(simple_interest(10000, 0.1, 10))

# Password strength score


def password_strength(password: str):
    le = len(password)
    ll = 0
    ul = 0
    d = 0
    sc = 0

    for i in password:
        if password.count(i) != 1:
            password = password.replace(i, '', password.count(i) - 1)
        if i.islower() and i.isalpha():
            ll += 1
        elif i.isupper() and i.isalpha():
            ul += 1
        elif i.isdigit():
            d += 1
        else:
            sc += 1

    if le != 0:
        s1 = str(le) + ' for each symbol'
    else:
        s1 = ''

    if ll != 0:
        s2 = ' + ' + str(ll) + ' * 2 for each lowercase letter'
    else:
        s2 = ''

    if ul != 0:
        s3 = ' + ' + str(ul) + ' * 3 for each uppercase letter'
    else:
        s3 = ''

    if d != 0:
        s4 = ' + ' + str(d) + ' * 4 for each digit'
    else:
        s4 = ''

    if sc != 0:
        s5 = ' + ' + str(d) + ' * 5 for each special character'
    else:
        s5 = ''

    print(str(le + 2 * ll + 3 * ul + 4 * d + 5 * sc) + ' # ' + s1 + s2 + s3 +
          s4 + s5)


string = input('Enter a password: ')
password_strength(string)

# Caesar cipher


def encrypt(message, shift):
    ciphertext = ''

    for i in message:
        if 65 <= ord(i) <= 90:  # Capital letters of the English alphabet
            ciphertext = ciphertext + chr((ord(i) - 65 + shift) % 26 + 65)
        elif 97 <= ord(i) <= 122:  # Lowercase letters of the English alphabet
            ciphertext = ciphertext + chr((ord(i) - 97 + shift) % 26 + 97)
        elif 1040 <= ord(i) <= 1071:  # Сapital letters of the Ukrainian
            ciphertext = ciphertext + chr((ord(i) - 1040 + shift) % 32 + 1040)
        elif 1072 <= ord(i) <= 1103:  # Lowercase letters of the Ukrainian
            ciphertext = ciphertext + chr((ord(i) - 1072 + shift) % 32 + 1072)
        else:
            ciphertext = ciphertext + i

    return ciphertext


def decrypt(encrypted_message, shift):
    plaintext = ''

    for i in encrypted_message:
        if 65 <= ord(i) <= 90:  # Capital letters of the English alphabet
            plaintext = plaintext + chr((ord(i) - 65 - shift) % 26 + 65)
        elif 97 <= ord(i) <= 122:  # Lowercase letters of the English alphabet
            plaintext = plaintext + chr((ord(i) - 97 - shift) % 26 + 97)
        elif 1040 <= ord(i) <= 1071:  # Сapital letters of the Ukrainian
            plaintext = plaintext + chr((ord(i) - 1040 - shift) % 32 + 1040)
        elif 1072 <= ord(i) <= 1103:  # Lowercase letters of the Ukrainian
            plaintext = plaintext + chr((ord(i) - 1072 - shift) % 32 + 1072)
        else:
            plaintext = plaintext + i

    return plaintext


str1 = encrypt('The quick brown fox jumps over the lazy dog ;)', 23)
str2 = decrypt(str1, 23)

print(str1)
print(str2)
