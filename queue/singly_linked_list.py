class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        current_value = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        self.length -= 1
        return current_value

    def remove_tail(self):
        if self.tail is None and self.head is None:
            return None
        elif self.head is self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            current_node = self.head
            old_tail = self.tail.get_value()
            while current_node.get_next() is not self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            self.tail.set_next(new_next=None)
            self.length -= 1
            return old_tail

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if value == current_node.get_value():
                return True
            current_node = current_node.get_next()
        return False

    def get_max(self):
        cur_max = self.head.get_value()
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() > cur_max:
                cur_max = current_node.get_value()
            current_node = current_node.get_next()
        return cur_max
