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

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head == None:
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
        result = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        result.delete()
        if self.length > 0:
            self.length -= 1
        return result.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail == None:
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
        result = self.tail
        self.tail = self.tail.prev
        if self.tail == None:
            self.head = None
        result.delete()
        if self.length > 0:
            self.length -= 1
        return result.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.length == 1:
            pass
        if self.tail == node:
            self.tail = self.tail.prev
        node.delete()
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.head.prev = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.length == 1:
            pass
        if self.head == node:
            self.head = self.head.next
        node.delete()
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        node.delete()
        if self.length > 0:
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        curr_node = self.head
        curr_max = self.head.value
        while curr_node != None:
            if curr_node.value > curr_max:
                curr_max = curr_node.value
            curr_node = curr_node.next
        return curr_max
