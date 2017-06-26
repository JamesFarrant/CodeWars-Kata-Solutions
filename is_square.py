from math import sqrt
def is_square(n):
    return n == int(sqrt(n)) * int(sqrt(n)) if n >= 0 else False
