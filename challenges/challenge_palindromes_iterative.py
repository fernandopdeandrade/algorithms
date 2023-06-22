palindrome = "lava esse aval"
not_palindrome = "lava esse avall"


def is_palindrome_iterative(word: str) -> bool:
    if word == "":
        return False

    low_index = 0
    high_index = len(word) - 1

    while low_index < high_index:
        if word[low_index] != word[high_index]:
            return False

        low_index += 1
        high_index -= 1

    return True


print(is_palindrome_iterative(palindrome))
print(is_palindrome_iterative(not_palindrome))
