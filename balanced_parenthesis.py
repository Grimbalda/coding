# Balanced parenthesis
#
# Create function that will determine are the parenthesis balanced in a given string
# boolean isBalanced(string)
#
# a(bcd)d => true
# (kjds(hfkj)sdhf => false
# (sfdsf)(fsfsf => false
#
# {[]}() => true
# {[}] => false


# My questions:
# What kinds of parenthesis can I expect in the input string? Only one kind or multiple kinds?

# What to check:
#   Are all parenthesis closed
#   If the found closing parenthesis matches the last one opened

# Edge cases:
#   No parenthesis in string
#   Only closing parenthesis
#   Parenthesis pair when the first one is closing and the second one is opening


import sys


def is_balanced(string):
    close_open_map = {'}': '{',
                      ']': '[',
                      ')': '('}
    opened_parenthesis = []
    for char in string:
        if char in ['[', '(', '{']:
            opened_parenthesis.append(char)
        elif char in [']', ')', '}']:
            open_pair = close_open_map[char]
            if opened_parenthesis and opened_parenthesis[-1] == open_pair:
                opened_parenthesis.pop()
            else:
                return False
    return not bool(len(opened_parenthesis))


if __name__ == '__main__':
    print is_balanced(sys.argv[1])
