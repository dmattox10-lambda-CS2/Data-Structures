"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value >= self.value:  # Am I supposed to do this?
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        elif target == self.value:
            return True
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        max = self.value
        current = self
        while current.right is not None:
            max = current.right.value
            current = current.right
        return max

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Queue

    def bft_print(self):
        # grab root
        q = Queue()
        q.enqueue(self)
        while len(q) > 0:
            # if items in queue, dequeue current node
            current = q.dequeue()
        # mark current node as visited
            # ???
        # print the value
            print(current.value)
        # check left
            if current.left is not None:
                # enqueue the left
                q.enqueue(current.left)
        # check right
            if current.right is not None:
                # enqueue the right
                q.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Stack
    from stack import Stack

    def dft_print(self):
        s = Stack()
        s.push(self)
        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left is not None:
                s.push(current.left)
            if current.right is not None:
                s.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
