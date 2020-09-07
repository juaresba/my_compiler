def is_space(char):
    space_set = frozenset({' ', '\t', '\v', '\r', '\n', '\f'})
    return char in space_set

def is_alpha(char):
    return char.isalpha()    

def is_digit(char):
    return char.isdigit()

def is_alnum(char):
    return char.isalnum()