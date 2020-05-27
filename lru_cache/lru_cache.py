"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def find_middle(self):
        middle = self.head
        end = self.head

        while end != None and end.next.next != None:
            end = end.next.next
            middle = middle.next

        return middle

    def reverse_list(self):
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.length < 1:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        if not self.tail:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

        return value

    """Wraps the given value in a ListNode andkjjj;jj;j;j;j;uouoou inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.length < 1:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        if not self.tail:
            return
        elif self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head:
            return

        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None

        if node == self.head:
            self.head = node.next
            self.head.prev = None
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.delete()

    def get_max(self):
        # Walk through entire list
        # Keep track of highest value

        highest_value = self.head.value
        current_node = self.head

        while current_node is not None:
            if current_node.value > highest_value:
                highest_value = current_node.value
            current_node = current_node.next

        return highest_value


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.max_nodes = limit
        self.current_nodes = 0
        self.dll = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.dict:
            return
        node = self.dll.head
        while node is not None:
            if key == node.value[0]:
                self.dll.move_to_front(node)
                break
            node = node.next
        return self.dict[key]
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, val):
        # if key is already stored, overwrite old value
        # otherwise, add to cache
        # handle case where we are already full
        if key in self.dict:
            self.dict[key] = val
            # Overwrite DLL
            node = self.dll.head
            while node is not None:
                if key == node.value[0]:
                    # update val [key, value]
                    node.value[1] = val
                    self.dll.move_to_front(node)
                    break
                node = node.next
        else:
            if self.current_nodes == self.max_nodes:
                node = self.dll.tail
                old_key = node.value[0]
                self.dll.remove_from_tail()

                del self.dict[old_key]
                self.current_nodes -= 1

            self.dict[key] = val
            self.dll.add_to_head([key, val])
            self.current_nodes += 1
