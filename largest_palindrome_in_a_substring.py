def is_palindrome(string):
    return string == string[::-1]


def find_largest_palindrome(string):
    max_length = 0
    largest_palindrome = ''
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if is_palindrome(string[i:j]):
                if j - i > max_length:
                    max_length = j - i
                    largest_palindrome = string[i:j]
    return largest_palindrome


print(find_largest_palindrome('apsamadamaps'))
