# №1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def check_uniqe_letters(s):
    return len(s) == len(set(s))


def check_uniqe_letters_sort(s):
    list_s = list(s)
    list_s.sort()
    last = ""
    for letter in list_s:
        if letter == last:
            return False
        last = letter

    return True


# №2
# Check Permutation: Given two strings, write a method
# to decide if one is a permutation of the other.


def check_permutations(s1, s2):
    letters = {}
    for letter in s1:
        letters[letter] = letters.get(letter, 0) + 1

    for letter in s2:
        if letter not in letters:
            return False
        letters[letter] -= 1
        if letters[letter] < 0:
            return False
    return True


# №3
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
def replace_space(s):
    return s.strip().replace(" ", "%20")


# №4
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
def check_permutations_palindrome(s):
    letters = {}
    s = s.replace(" ", "")
    s = s.lower()
    for letter in s:
        letters[letter] = letters.get(letter, 0) + 1

    flag = False
    for letter in letters:
        if letters[letter] % 2 == 1:
            if flag:
                return False
            flag = True
    return True


# №5
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def check_insert_delete_replace(s1, s2):
    """
    insert: len + 1
    delete: len - 1
    replace: same len
    """

    def one_edit_replace(s1, s2):
        flag = False
        for a, b in zip(s1, s2):
            if a != b:
                if flag:
                    return False
                flag = True
        return True

    def one_edit_insert(s1, s2):
        i = 0
        j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if i != j:
                    return False
                i += 1
            else:
                i += 1
                j += 1
        return True

    result = False
    if len(s1) == len(s2):
        result = one_edit_replace(s1, s2)
    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) > len(s2):
            result = one_edit_insert(s1, s2)
        else:
            result = one_edit_insert(s2, s1)
    return result


# №6

# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def shorten_string(s):
    if not s:
        return s
    count = 1
    answer = ""
    last_letter = s[0]
    for i in range(1, len(s)):
        if s[i] == last_letter:
            count += 1
        else:
            answer += last_letter + str(count)
            count = 1
            last_letter = s[i]
    answer += last_letter + str(count)
    return answer if len(answer) < len(s) else s


# №7
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_matrix(mtx):
    ans = []
    for line in zip(*mtx):
        ans.append(list(line[::-1]))
    return ans


import copy


# №8
# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.


def make_null_matrix(mtx):
    answer = copy.deepcopy(mtx)

    def make_null_row(index):
        for j in range(len(mtx[0])):
            answer[index][j] = 0

    def make_null_col(index):
        for i in range(len(mtx)):
            answer[i][index] = 0

    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 0:
                make_null_row(j)
                make_null_col(i)
    return answer


# №9
# 9 String Rotation; Assume you have a method isSubs t rin g which checks if one word is a substring
# of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
# call to isSubs t rin g [e.g., "wate r bottle " is a rotation oP'erbottlewat")


def check_shifted_substring(s1, s2):
    if len(s1) == len(s2):
        return s2 in s1 + s1
    return False


if __name__ == "__main__":
    s1 = "stringsud"
    s2 = "substring"
    print(check_shifted_substring(s1, s2))
