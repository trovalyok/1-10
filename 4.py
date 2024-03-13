# Area of a Triangle Given its Vertices
def triangle_area(x1, y1, x2, y2, x3, y3):
    Area = 1/2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return Area


x1 = float(input('Enter a x-axis coordinate of the first vertice: '))
y1 = float(input('Enter a y-axis coordinate of the first vertice: '))
x2 = float(input('Enter a x-axis coordinate of the second vertice: '))
y2 = float(input('Enter a y-axis coordinate of the second vertice: '))
x3 = float(input('Enter a x-axis coordinate of the third vertice: '))
y3 = float(input('Enter a y-axis coordinate of the third vertice: '))

print('Area of the triangle:', triangle_area(x1, y1, x2, y2, x3, y3))

# Count a number of words in the sentence
sentence = "Гаррі Поттер (англ. Harry Potter) — серія\
 з семи фантастичних романів англійської письменниці..."
list_of_words = sentence.split()
count = 0

for i in range(len(list_of_words)):
    if any(symbol.isalpha() for symbol in list_of_words[i]):
        count = count + 1

print('The number of words in this sentence is ', count)

# snake_case to CamelCase convertor
case_start_string = "snake_case_text"
end_string = case_start_string.title().replace('_', '')
print(end_string)

# FizzBuzz
number = input('Enter a positive natural number: ')
while number.isdigit() is False or int(number) == 0:
    print("That's not a positive natural number!")
    number = input('Enter a positive natural number: ')
number = int(number)


def fizz_buzz(n):
    list_of_numbers = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list_of_numbers.append('FizzBuzz')
        elif i % 3 == 0:
            list_of_numbers.append('Fizz')
        elif i % 5 == 0:
            list_of_numbers.append('Buzz')
        else:
            list_of_numbers.append(i)
    return list_of_numbers


print(fizz_buzz(number))

# snake_case to CamelCase convertor
start_string = "SnakeCaseText"
index = 0

while index < len(start_string):
    if start_string[index].isupper() and index != 0:
        start_string = start_string[:index] + '_' + start_string[index:]
        index += 1
    index += 1

end_string = start_string.lower()
print(end_string)

# Anagrams
str1 = input('Enter a first string: ')
str2 = input('Enter a second string: ')


def anagrams1(s1, s2):
    for i in s1:
        if i in s2:
            s1 = s1.replace(i, "", 1)  # delete only the first occurrence
            s2 = s2.replace(i, "", 1)
    return not bool(s1) and not bool(s2)


print('Two strings are anagrams1 -', anagrams1(str1, str2))


def anagrams2(s1, s2):
    return sorted(s1) == sorted(s2)


print('Two strings are anagrams2 -', anagrams2(str1, str2))
