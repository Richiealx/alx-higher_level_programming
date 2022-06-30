#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == "__main__"):
    argc = len(argv)
    result = 0
    operators = ["+", "-", "*", "/"]

    if (argc != 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    if (argv[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
