#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        answer = a / b
    except (TypeError, ZeroDivisionError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
    return (answer)
