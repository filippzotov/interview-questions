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
