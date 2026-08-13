'''Practice: Functions (logic-focused, low math)

Work through these one at a time. Each function has a short spec and a
couple of print() calls below it so you can check your own output as you go.
No hints given up front on purpose — try first, then ask if you get stuck.
'''

# 1. is_palindrome(word)
#    Returns True if the given string reads the same forwards and backwards
#    (case-insensitive), False otherwise.
#    Example: "level" -> True, "Racecar" -> True, "python" -> False


def is_palindrome(word):
    pass


print(is_palindrome("level"))     # expected: True
print(is_palindrome("Racecar"))   # expected: True
print(is_palindrome("python"))    # expected: False


# 2. count_vowels(text)
#    Returns how many vowels (a, e, i, o, u - case-insensitive) appear in text.
#    Example: "Hello World" -> 3


def count_vowels(text):
    pass


print(count_vowels("Hello World"))   # expected: 3
print(count_vowels("PYTHON"))        # expected: 1
print(count_vowels(""))              # expected: 0


# 3. most_frequent_char(text)
#    Returns the character that appears the most times in text.
#    Assume no ties in the test cases below.
#    Example: "banana" -> "a"


def most_frequent_char(text):
    pass


print(most_frequent_char("banana"))     # expected: a
print(most_frequent_char("mississippi"))  # expected: i


# 4. remove_duplicates(items)
#    Takes a list and returns a new list with duplicates removed,
#    keeping the original order of first appearance.
#    Example: [1, 2, 2, 3, 1, 4] -> [1, 2, 3, 4]


def remove_duplicates(items):
    pass


print(remove_duplicates([1, 2, 2, 3, 1, 4]))   # expected: [1, 2, 3, 4]
print(remove_duplicates(["a", "b", "a", "c"]))  # expected: ['a', 'b', 'c']


# 5. flatten(nested_list)
#    Takes a list of lists and returns a single flat list.
#    Example: [[1, 2], [3], [4, 5, 6]] -> [1, 2, 3, 4, 5, 6]


def flatten(nested_list):
    pass


print(flatten([[1, 2], [3], [4, 5, 6]]))   # expected: [1, 2, 3, 4, 5, 6]
print(flatten([["a"], ["b", "c"]]))        # expected: ['a', 'b', 'c']


# 6. caesar_shift(text, shift)
#    Shifts each lowercase letter in text forward by `shift` positions in
#    the alphabet, wrapping around from 'z' back to 'a'. Leave non-letters
#    (spaces, punctuation, uppercase) unchanged. Assume shift is 0-25.
#    Example: caesar_shift("abc xyz", 2) -> "cde zab"
#    (This uses ord()/chr() rather than arithmetic on the "value" itself,
#    so it's more about character logic than math.)


def caesar_shift(text, shift):
    pass


print(caesar_shift("abc xyz", 2))   # expected: cde zab
print(caesar_shift("hello", 1))     # expected: ifmmp
