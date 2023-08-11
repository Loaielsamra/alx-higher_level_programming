#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    length = len(argv) - 1
    if (length < 3):
        printf("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv(1))
    b = int(argv(3))
    op = argv(2)

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    final = operators[op](a, b)

    print("{} {} {} = {}".format(a, op, b, final))
