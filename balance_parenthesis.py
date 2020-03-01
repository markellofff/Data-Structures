"""
Here we check the given string of parenthesis is balanced or not
Balanced Parenthesis:
'[{()}]'
:return true

Un-Balanced Parenthesis:
'[)[]}'
:return false

For this we need to use the stack so import the Stack class from stack.py
"""

from stack import Stack


def matched_paren(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_balanced_paren(paren_string):
    # Check for the empty String
    if not paren_string.strip(): return 'Empty String'

    index = 0
    is_balanced = True
    # initializing the Stack
    s = Stack()
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '({[':
            s.push(paren)
        else:
            if s.stack_length() == 0:
                is_balanced = False
            else:
                top = s.peek()
                s.pop()
                if not matched_paren(top, paren):
                    is_balanced = False
        index += 1

    if s.stack_length() == 0 and is_balanced:
        return True
    else:
        return False


print(is_balanced_paren(str))
