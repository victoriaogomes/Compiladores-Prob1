import re

def is_delimiter(c):
    if c == '(' or c == ')' or c == '{' or c == '}' or c == '[' or c == ']' or c == ';' or c == ',' or c == '.':
        return True
    else:
        return False


def is_char(c):
    if re.search(r"[a-z]|[A-Z]", c):
        return True
    else:
        return False


def is_logic_operator(c):
    if c == '&' or c == '|' or c == '!':
        return True
    else:
        return False


def is_arithmetic_operator(c):
    if c == '+' or c == '-' or c == '*' or c == '/':
        return True
    else:
        return False


def is_relacional_operator(c):
    if c == '!' or c == '=' or c == '>' or c == '<':
        return True
    else:
        return False


