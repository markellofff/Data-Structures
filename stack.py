"""
Implementing Stack using python
D
C
B
A
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return f"Item {item} pushed in the Stack"

    def stack_length(self):
        return len(self.items)

    def pop(self):
        if self.stack_length() != 0:
            self.items.pop(-1)
            return f"Item Popped"
        else:
            return 'Stack is Empty'

    def print_stack(self):
        return self.items


s = Stack()

s.push('A')
s.push('B')
s.push('C')
s.push('D')
print(s.stack_length())
print(s.print_stack())
s.pop()
print(s.stack_length())
print(s.print_stack())
