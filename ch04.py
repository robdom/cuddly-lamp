def numsquared(num):
    """
    Returns num * num.
    :param num: int.
    :return: int product of num * num.
    """
    return num * num

print(numsquared(12))

def printstr(str):
    """
    Prints str.
    :param str: str.
    """
    print(str)

print(printstr("What's up?"))

def knicks(a, b, c, d=5, e=1):
    """
    Prints number of Knicks guards, wings, bigs, assistants, and trainers
    for 2018-2019.
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int. (optional)
    :param e: int. (optional)
    :return: str.
    """
    print(f"The Knicks have {a} guards, {b} wings, {c} bigs, {d} assistants, and {e} trainers under contract in 2018-2019.")

knicks(6, 6, 3)

def divide_by_two(a):
    """
    Returns a / 2.
    :param a: int.
    :return int or float quotient of a / 2.
    """
    return a / 2

def multiply_by_four(b):
    """
    Returns b * 4.
    :param b: int.
    :return int of b * 4.
    """
    return b * 4

result = divide_by_two(4)

print(multiply_by_four(result))

def convert_str_to_float(str):
    """
    Returns result of converting a string to a float.
    :param str: int or float.
    :return float of float(str)
    """
    try:
        return float(str)
    except ValueError:
        print("String can only contain numbers and decimal points")

print(convert_str_to_float("Hello, World!"))
