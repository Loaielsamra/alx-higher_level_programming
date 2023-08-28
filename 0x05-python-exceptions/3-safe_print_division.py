#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        print("Inside Result: ", end="")
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print(result)
    return result

