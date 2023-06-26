from data_structures import LinkedList


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class Simple_LL:
    def __init__(self, vals=None) -> None:
        self.head = Node()
        cursor = self.head
        if vals:
            for val in vals:
                cursor.val = val
                cursor.next = Node()
                cursor = cursor.next

    def __str__(self):
        cursor = self.head
        answer = ""
        while cursor.next:
            answer += str(cursor.val) + " "
            cursor = cursor.next
        return answer


# №1
# Remove Dups: Write code to remove duplicates from an unsorted linked list
def remove_dups_old(linked_list):
    if not linked_list.head:
        return linked_list
    head = linked_list.head
    visited = set()
    while head:
        if head.val in visited:
            linked_list.delete(head.val)
        else:
            visited.add(head.val)
        head = head.next


def remove_dups(LL):
    prev = None
    cursor = LL.head
    visited = set()
    while cursor:
        if cursor.val in visited:
            prev.next = cursor.next

        else:
            visited.add(cursor.val)
            prev = cursor
        cursor = cursor.next


# 2
# Return Kth to Last: Implement an algorithm to find
# the Kth to last element of a singly linked list.
def get_k_to_last(LL, k):
    cur1 = LL.head
    cur2 = LL.head
    for _ in range(k):
        cur2 = cur2.next

    while cur2.next:
        cur2 = cur2.next
        cur1 = cur1.next

    return cur1.val


# №3
# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
def delete_middle_node(node):
    if node == None or node.next == None:
        return
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next


# №4
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.


def make_partition(LL, x):
    cur = LL.head
    before = []
    after = []
    while cur.next:
        if cur.val < x:
            before.append(cur.val)
        else:
            after.append(cur.val)
        cur = cur.next
    before.extend(after)
    return Simple_LL(before)


# 5
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.


# string way
def sum_lists(LL1, LL2):
    cur = LL1.head
    num1 = ""
    while cur.next:
        num1 = str(cur.val) + num1
        cur = cur.next

    cur = LL2.head
    num2 = ""
    while cur.next:
        num2 = str(cur.val) + num2
        cur = cur.next

    return sum([int(num1), int(num2)])


# 6
# Palindrome: Implement a function to check if a linked list is a palindrome.
def check_palindrome_list(LL):
    slow = LL.head
    fast = LL.head
    half = []
    while fast and fast.next:
        half.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if not fast:
        half = half[:-1]
    for num in half[::-1]:
        if num != slow.val:
            return False
        slow = slow.next
    return True


# 7
# Intersection; Given two (singly) linked lists, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jt h node of the second
# linked list, then they are intersecting.
def find_intersection(LL1, LL2):
    def get_len_and_last(LL):
        count = 0
        cur = LL.head
        while cur.next:
            count += 1
            cur = cur.next
        return (count, cur)

    def get_intersection_node(bigger, smaller, dif):
        cur1 = bigger.head
        cur2 = smaller.head
        for _ in range(dif):
            cur1 = cur1.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

    lenLL1, last1 = get_len_and_last(LL1)
    lenLL2, last2 = get_len_and_last(LL2)
    if last1 != last2:
        return False
    dif = abs(lenLL1 - lenLL2)
    if lenLL1 > lenLL2:
        ans = get_intersection_node(LL1, LL2, dif)
    else:
        ans = get_intersection_node(LL2, LL1, dif)

    return ans


# 8
# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
def find_loop_start(LL):
    cur = LL.head
    fast = LL.head
    while fast and fast.next:
        cur = cur.next
        fast = fast.next.next
        if cur == fast:
            break
    if not fast or not fast.next:
        return False
    cur = LL.head
    while cur != fast:
        cur = cur.next
        fast = fast.next
    return cur


if __name__ == "__main__":
    vals = [1, 2, 1, 2, 5, 5, 7, 1, 1, 1, 7, 7, 6, 6]

    # LL = Simple_LL(vals)
    # print(LL)
    # remove_dups(LL)
    # print(LL)
    # vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # LL = Simple_LL(vals)
    # print(LL)

    # cur = LL.head.next.next.next
    # print(cur.val)
    # delete_middle_node(cur)
    # print(LL)

    # vals = [3, 5, 8, 5, 10, 2, 1]
    # LL = Simple_LL(vals)
    # print(LL)
    # LL = make_partition(LL, 5)
    # print(LL)

    # vals1 = [7, 1, 6]
    # vals2 = [5, 9, 2]
    # LL1 = Simple_LL(vals1)
    # LL2 = Simple_LL(vals2)

    # print(sum_lists(LL1, LL2))
    # vals1 = [3, 1, 5, 9, 7, 2, 1]
    # vals2 = [4, 6]
    # LL1 = Simple_LL(vals1)
    # LL2 = Simple_LL(vals2)
    # cur = LL2.head
    # cur = cur.next
    # f1 = LL1.head.next.next.next
    # print(f1)
    # cur.next = f1
    # print(LL1)
    # print(LL2)
    # print(find_intersection(LL1, LL2).val)
