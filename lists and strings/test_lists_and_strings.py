from lists_and_strings import *
import pytest


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("abcd", True),
        ("abcdeig", True),
        ("aaaabbbbccc", False),
        ("letter", False),
        ("key", True),
    ),
)
def test_check_uniqe_letters(input, expected):
    assert check_uniqe_letters(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("abcd", True),
        ("abcdeig", True),
        ("aaaabbbbccc", False),
        ("letter", False),
        ("key", True),
    ),
)
def test_check_uniqe_letters_sort(input, expected):
    assert check_uniqe_letters_sort(input) == expected


@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    (
        ("abc", "abc", True),
        ("abc", "cab", True),
        ("abbts", "aabx", False),
        ("", "", True),
        ("pytesttest", "testpytset", True),
    ),
)
def test_check_permutations(s1, s2, expected):
    assert check_permutations(s1, s2) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("Test case one", "Test%20case%20one"),
        ("Test   case  two     ", "Test%20%20%20case%20%20two"),
        ("", ""),
    ),
)
def test_replace_space(input, expected):
    assert replace_space(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("test tset", True),
        ("bobo", True),
        ("not palindrome", False),
        ("Print intpr", True),
    ),
)
def test_check_permutations_palindrome(input, expected):
    assert check_permutations_palindrome(input) == expected


@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    (
        ("cake", "cake", True),
        ("cake", "bake", True),
        ("cake", "cak", True),
        ("cake", "cakee", True),
        ("cake", "cat", False),
    ),
)
def test_check_insert_delete_replace(s1, s2, expected):
    assert check_insert_delete_replace(s1, s2) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("aaaa", "a4"),
        ("abcd", "abcd"),
        ("aabbbcc", "a2b3c2"),
        ("zzbb", "zzbb"),
    ),
)
def test_shorten_string(input, expected):
    assert shorten_string(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[1]], [[1]]),
    ),
)
def test_rotate_matrix(input, expected):
    assert rotate_matrix(input) == expected


def test_make_null_matrix():
    matrix = [[1 for _ in range(3)] for _ in range(3)]
    matrix[1][1] = 0
    expected = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    assert make_null_matrix(matrix) == expected


@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    (
        ("substring", "stringsub", True),
        ("thequickbrownfox", "kbrownfoxthequic", True),
        ("substring", "stringsut", False),
    ),
)
def test_check_shifted_substring(s1, s2, expected):
    assert check_shifted_substring(s1, s2) == expected
