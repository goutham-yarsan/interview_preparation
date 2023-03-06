def find_non_repetitive_char(string):
    for i in range(len(string)):
        count = 1
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                count += 1
        if count == 1:
            return string[i]


print(find_non_repetitive_char('reddy'))


def test_find_non_repetitive_char():
    assert find_non_repetitive_char('reddy') == 'r'
