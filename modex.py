from math import floor
from math import pow


def modex(x, y, z):
    """
    :param x: the base
    :param y: the exponent
    :param n: the mod variable
    :return: x^y mod n
    """
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
