"""
Stack Using SLL(singly linked list)
"""


class Node:
    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # for setting data
    def set_data(self, data):
        self.data = data

    # for getting data
    def get_data(self):
        return self.data

    # for setting next
    def set_next(self, next_data):
        self.next = next_data

    # for getting next
    def get_next(self):
        return self.next

    # returns true if the node is pointing to another node
    def has_next(self):
        return self.next is not None


class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def peek(self):
        if self.head is None: raise IndexError
        return self.head.get_data()

    def stack_length(self):
        if self.head is None: return 'Empty Stack'
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.get_next()
        return count

    def print_stack(self):
        if self.head is None: return 'Empty Stack'
        temp = self.head
        stack = []
        while temp is not None:
            stack.append(temp.get_data())
            temp = temp.get_next()
        return stack

# our_list = [1, 2, 3]
# our_stack = Stack(our_list)  # [3, 2, 1]
# print(our_stack.print_stack())  # [[3, 2, 1]
# our_stack.push(15)  # [15, 3, 2, 1]
# print(our_stack.print_stack())  # [15, 3, 2, 1]
# print(our_stack.pop())  # 15
# print(our_stack.print_stack())  # [3, 2, 1]
