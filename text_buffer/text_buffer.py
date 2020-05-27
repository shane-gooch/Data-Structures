
# add to the back of a text buffer
# add to the front of a text buffer
# delete the back of a text buffer
# delete the front of a text buffer
# join text buffers together -
# add to the middle

# array vs DLL

# array: add to back O(1)
# array: add from front:O(n)
# array: delete to back O(1)
# array: delete from front:O(n)
# array: join together = O(n)

# **faster to use a DLL
# DLL: add to back: O(1)
# DLL: add to front O(1)
# DLL: delete to back: O(1)
# DLL: delte to front O(1)
# array: join together = O(1)

# __str__, to print what's inside
# array, O(n)
# DLL, O(n)
from doubly_linked_list import DoublyLinkedList
import sys
sys.path("../doubly_linked_list")


class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __str__(self):
        string_to_return = ""
        node = self.storage.head
        while node is not None:
            string_to_return += node.value
            node = next.next
        return string_to_return

    def join(self, other_buffer):
        # Link tail of current buffer to head of other buffer
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        # Point current buffer to its new tail
        self.storage.tail = self.storage.tail

    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)

    def delete_from_front(self, num_of_chars_to_remove):
        for _x in range(num_of_chars_to_remove):
            self.storage.remove_from_head()

    def delete_from_back(self, num_of_chars_to_remove):
        for _x in range(num_of_chars_to_remove):
            self.storage.remove_from_head()

    def find_text(self, text_to_find):
        pass
