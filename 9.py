# Difference between two lists


def compute_difference(first: list, second: list) -> tuple:
    first_second = first[:]
    second_first = second[:]
    for item in first_second:
        for item in second_first:
            if item in first_second:
                first_second.remove(item)
                second_first.remove(item)
    return (first_second, second_first)


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])

    result4 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result4 == ([1], [4])

    result5 = compute_difference([1, 2, 3], [])
    assert result5 == ([1, 2, 3], [])


list1 = ['a', 'b', 'c', 'd']
list2 = ['c', 'd', 'e']
print(f"Difference between {list1} & {list2}\
 is {compute_difference(list1, list2)}")

test_compute_difference()

# Indices of additions


def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 9)
    assert result1 == [0, 1]

    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]

    result3 = sum_of_two([3, 3], 6)
    assert result3 == [0, 1]

    result4 = sum_of_two([3, 2], 6)
    assert result4 is None


list_of_integers = [1, 2, 9, 4, 6]
total = 7
print(f"In the {list_of_integers}, the numbers with\
 {sum_of_two(list_of_integers, total)} indices add up to {total}.")

test_sum_of_two()

# Unique elements


def unique_elements(arr: list) -> list:
    a = []
    [a.append(i) for i in arr if arr.count(i) == 1]
    return a


def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]

    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]

    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


list_of_elements = [1, 2, 9, 4, 6, 5, 5, 5, 9]
print(f"In the given list {list_of_elements}, elements\
 {unique_elements(list_of_elements)} are unique.")

test_unique_elements()

# Elements that appear an odd number of times


def odd_elements(arr: list) -> list:
    a = []
    [a.append(i) for i in arr if arr.count(i) % 2 == 1 and i not in a]
    return a


def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]

    result2 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result2 == [1, 3, 4, 6]


print(f"In the given list {list_of_elements}, elements\
 {odd_elements(list_of_elements)} occur an odd number of times.")

test_odd_elements()

# A second-largest element in the list


def second_largest_element(arr: list) -> int:
    a = arr[:]
    if min(a) != max(a):
        a.remove(max(a))
        return max(a)
    else:
        return None


def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5

    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4

    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 is None


print(f"In the {list_of_integers},\
 {second_largest_element(list_of_integers)} is the second-largest element.")

test_second_largest_element()

# Sort a list by population, calculate average and total population

city_population = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]


def population(v):
    return v[1]


city_population.sort(key=population)
print(city_population)

s = sum(population(i) for i in city_population)
avg = s / len(city_population)

print(f"Average population is {avg}")
print(f"Total population is {s}")
