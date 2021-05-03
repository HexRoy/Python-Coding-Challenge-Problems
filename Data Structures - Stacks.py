# Simple Stack class
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# Data structure tutorial exercise: Stack
# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
# Solution

string_to_reverse = "We will conquer COVID-19"
stack = Stack()
for letter in string_to_reverse:
    stack.push(letter)

reversed_string = ""
while not stack.is_empty():
    reversed_string += stack.pop()
print(reversed_string)


# Write a function in python that checks if paranthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def is_balanced(s):
    stack_2 = Stack()
    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack_2.push(char)
        elif char == ")":
            if stack_2.is_empty():
                return False
            if stack_2.pop() != "(":
                return False
        elif char == "}":
            if stack_2.is_empty():
                return False
            if stack_2.pop() != "{":
                return False
        elif char == "]":
            if stack_2.is_empty():
                return False
            if stack_2.pop() != "[":
                return False
    return True


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
