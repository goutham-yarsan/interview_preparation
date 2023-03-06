# numbers = [int(item) for item in input('enter a list of numbers:').split()]
# smallest = numbers[0]
# second_smallest = numbers[1]
# for num in numbers:
#     if num < smallest:
#         smallest, second_smallest = num, smallest
#     elif num < second_smallest:
#         second_smallest = num
# print(second_smallest)


def find_second_smallest_number(numbers):
    smallest = numbers[0]
    second_smallest = numbers[1]
    for num in numbers:
        if num < smallest:
            smallest, second_smallest = num, smallest
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


print(find_second_smallest_number([1, 2, 3, 4, 0, -2, -1, -5]))


def test_find_second_smallest_number():
    assert find_second_smallest_number([1, 2, 3, 4, 0, -2, -1, -5]) == -5
