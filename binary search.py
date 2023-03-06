def find_value(numbers, number_to_find):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        middle = (high + low) // 2

        if numbers[middle] == number_to_find:
            return middle
        elif numbers[middle] < number_to_find:
            low = middle + 1
        else:
            high = middle - 1
    return 'not found'


print(find_value([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))