# №1
# Реализуйте алгоритм, определяющий, все ли символы в строке встречаются
# только один раз. А если при этом запрещено использование дополнительных
# структур данных?


# 82
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
# Для двух строк напишите метод, определяющий, является ли одна строка
# перестановкой другой .


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
#  Напишите метод, заменяющий все пробелы в строке символами • %20 •.
def replace_space(s):
    return s.strip().replace(" ", "%20")


# №4
# Напишите функцию, которая проверяет, является ли заданная строка перестановкой палиндрома. (Палиндром - слово или фраза, одинаково читающиеся
# в прямом и обратном направлении; перестановка - строка, содержащая те
# же символы в другом порядке.) Палиндром не ограничивается словами из
# словаря.
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
# Существуют три вида модифицирующих операций со строками: вставка
# символа, удаление символа и замена символа. Напишите функцию, которая
# проверяет, находятся ли две строки на расстоянии одной модификации (или
# нуля модификаций).


def check_insert_delete_replace(s1, s2):
    """
    insert: len + 1
    delete: len - 1
    replace: same len
    """
    if len(s1) == len(s2):
        flag = False
        for let1, let2 in zip(s1, s2):
            if let1 != let2:
                if flag:
                    return False
                flag = True
    else:
        if abs(len(s1) - len(s2)) == 1:
            i1 = 0
            i2 = 0
            flag = False
            min_word = min(len(s1), len(s2))
            max_word = max(len(s1), len(s2))
            while i1 != max_word and i2 != max_word:
                if not flag:
                    if i1 == min_word or i2 == min_word:
                        return True
                if s1[i1] != s2[i2]:
                    if flag:
                        return False
                    flag = True
                    if len(s1) > len(s2):
                        i1 += 1
                    else:
                        i2 += 1
                i1 += 1
                i2 += 1
        else:
            return False
    return True


# №6

# Реализуйте метод для выполнения простейшего сжатия строк с использованием
# счетчика повторяющихся символов. Например, строка aabcccccaaa превращается
# в a2b1c5a3. Если 'сжатая' строка не становится короче исходной, то метод
# возвращает исходную строку.


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
# меется изображение, представленное матрицей NxN; каждый пиксел
# представлен 4 байтами. Напишите метод для поворота изображения на
# 90 градусов.
# Удастся ли вам выполнить эту операцию «На месте»?
def rotate_matrix(mtx):
    ans = []
    for line in zip(*mtx):
        ans.append(list(line[::-1]))
    return ans


import copy


# №8
# Напишите алгоритм, реализующий следующее условие: если элемент матрицы
# MxN равен О, то весь столбец и вся строка обнуляются.
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
# Допустим, что существует метод isSubstring, проверяющий, является ли
# одно слово подстрокой другого. Для двух строк sl и s2 напишите код, который
# проверяет, получена ли строка s2 циклическим сдвигом sl, используя
# только один вызов метода isSubstring
def check_shifted_substring(s1, s2):
    if len(s1) == len(s2):
        return s2 in s1 + s1
    return False


if __name__ == "__main__":
    s1 = "stringsud"
    s2 = "substring"
    print(check_shifted_substring(s1, s2))
