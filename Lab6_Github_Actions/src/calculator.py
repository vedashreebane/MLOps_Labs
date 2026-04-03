def add(x, y):
    #  Add two numbers.
    return x + y


def subtract(x, y):
    # Subtract y from x.
    return x - y


def multiply(x, y):
    # Multiply two numbers.
    return x * y


def combined(x, y):
    # Return the sum of add, subtract, and multiply results.
    return add(x, y) + subtract(x, y) + multiply(x, y)


def divide(x, y):
    # Divide x by y. Raises ValueError for division by zero.
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y