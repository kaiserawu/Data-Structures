import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.left == None and value < self.value:
            self.left = BinarySearchTree(value)
            return
        elif self.right == None and value > self.value:
            self.right = BinarySearchTree(value)
            return
        if value < self.value:
            self.left.insert(value)
        elif value > self.value:
            self.right.insert(value)
        return



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value and self.right != None:
            return self.right.contains(target)
        elif target < self.value and self.left != None:
            return self.left.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        if self.right != None:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bf_list = [self,]

        for item in bf_list:
            if item.left:
                bf_list.append(item.left)
            if item.right:
                bf_list.append(item.right)

        for item in bf_list:
            print(item.value)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
