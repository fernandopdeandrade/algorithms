def is_palindrome_recursive(
    word: str, low_index: int, high_index: int
) -> bool:
    if word == "" or low_index is None or high_index is None:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


print(is_palindrome_recursive("racecar", 0, 6))  # True
print(is_palindrome_recursive("racecar", 0, 5))  # False
