class ListNode(object):
    """Node class used for LinkedList."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def set_val(self, new_val):
        self.val = new_val

    def set_next(self, new_next):
        self.next = new_next

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next


class LinkedList:
    """Linked list class."""

    def __init__(self):
        # self.head = ListNode(val)
        # self.last = self.head
        self.head = None
        self.last = None

    def append(self, val):
        """Add new item to linked list."""
        if self.head:
            self.last.next = ListNode(val)
            self.last = self.last.next
        else:
            self.head = ListNode(val)
            self.last = self.head

    def display(self):
        """Return all elements of linked list as string, from oldest."""
        cursor = self.head
        output = "{ "
        while cursor:
            output += f"{str(cursor.get_val())}, "
            cursor = cursor.next
        output = output + " }"
        return output

    def size(self):
        """Counting size of linked list."""
        size = 0
        cursor = self.head
        while cursor:
            size += 1
            cursor = cursor.next
        return size

    def search(self, search_val):
        """Search for an value in linked list. Returns True if linked list contains value."""
        cursor = self.head
        while cursor:
            if cursor.val == search_val:
                return True
            cursor = cursor.next
        return False

    def delete(self, delete_val):
        """Delete value from linked list, if there is no such value, throughs ValueError."""
        prev = None
        cursor = self.head
        while cursor:
            if cursor.get_val() == delete_val:
                if prev:  # if it's not first node
                    if cursor == self.last:  # change pointer on last node
                        prev.next = None
                        self.last = prev
                    else:
                        prev.next = cursor.next
                    return
                else:  # if it's first node
                    self.head = cursor.next
                    return
            prev = cursor
            cursor = cursor.next
        else:
            raise ValueError("No such value")

    def insert(self, index, val):
        """Insert new value on specific index of Linked List,
        if index bigger that size of Linked List, append to the end."""
        size = self.size()
        if index > size:
            self.append(val)
        elif index == 1:
            tmp = self.head
            self.head = ListNode(val, tmp)
        else:
            cursor = self.head
            for _ in range(index - 2):
                cursor = cursor.next
            tmp = cursor.next
            cursor.next = ListNode(val, tmp)

    def __len__(self):
        return self.size()

    def __str__(self):
        return self.display()


class DoubleListNode:
    """Node class for Double Linked List."""

    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    """Double Linked List class."""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, val):
        """Add new item to the head of the list."""
        if not self.head:
            self.head = DoubleListNode(val)
            self.tail = self.head
        else:
            tmp = self.head
            self.head = DoubleListNode(val, prev=tmp)
            tmp.next = self.head

    def append_tail(self, val):
        """Add new item to the tail of the list."""
        if not self.tail:
            self.tail = DoubleListNode(val)
            self.head = self.tail
        else:
            tmp = self.tail
            self.tail = DoubleListNode(val, next=tmp)
            tmp.prev = self.tail

    def append_list(self, array):
        """Add list of items to the head of the list."""
        for element in array:
            self.append(element)

    def display(self):
        """Returns elements of Double linked list from tail to head in string format."""
        cursor = self.tail
        out = ""
        while cursor:
            out += str(cursor.val) + " "
            cursor = cursor.next
        return out

    def size(self):
        """Returns size of the Double linked list."""
        cursor = self.tail
        size = 0
        while cursor:
            size += 1
            cursor = cursor.next
        return size

    def pop_head(self):
        """Returns head element of the list and delete it"""
        if not self.head:
            raise IndexError("Nothing to pop")
        elif self.head == self.tail:
            pop_item = self.head.val
            self.head = None
            self.tail = None
            return pop_item
        else:
            pop_item = self.head.val
            self.head = self.head.prev
            self.head.next = None
            return pop_item

    def pop_tail(self):
        """Returns tail element of the list and delete it"""
        if not self.tail:
            raise IndexError("Nothing to pop")
        elif self.head == self.tail:
            pop_item = self.head.val
            self.head = None
            self.tail = None
            return pop_item
        else:
            pop_item = self.tail.val
            self.tail = self.tail.next
            self.tail.prev = None
            return pop_item

    def delete(self, delete_val):
        """Delete value from double linked list."""
        if not self.tail:
            raise ValueError("nothing to delete")
        cursor = self.tail

        while cursor:
            if cursor.val == delete_val:
                if cursor == self.head:
                    self.pop_head()
                elif cursor == self.tail:
                    self.pop_tail()
                else:
                    prev = cursor.prev
                    next = cursor.next
                    prev.next = next
                    next.prev = prev
            cursor = cursor.next

    def __str__(self) -> str:
        return self.display()

    def __len__(self):
        return self.size()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val)


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def __str__(self) -> str:
        return " ".join([str(i) for i in self.stack])
