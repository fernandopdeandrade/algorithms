def merge_string(left: str, right: str) -> str:
    result = ""
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result += left[left_index]
            left_index += 1
        else:
            result += right[right_index]
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result


def merge_sort_string(string: str) -> str:
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = merge_sort_string(string[:middle])
    right = merge_sort_string(string[middle:])

    return merge_string(left, right)


def is_anagram(first_string: str, second_string: str) -> tuple[str, str, bool]:
    if (
        type(first_string) != str
        or type(second_string) != str
        or len(first_string) == 0
        and len(second_string) == 0
    ):
        return (first_string, second_string, False)

    first_string = merge_sort_string(first_string.lower())
    second_string = merge_sort_string(second_string.lower())

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    for i in range(len(first_string)):
        if first_string[i] != second_string[i]:
            return (first_string, second_string, False)

    return (first_string, second_string, True)


# print(is_anagram("amor", "roma"))
# saída = ('amor', 'amor', True)
