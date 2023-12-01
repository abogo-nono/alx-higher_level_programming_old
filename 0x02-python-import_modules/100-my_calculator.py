#!/usr/bin/python3
import sys
from calculator_1 import add, sub,  mul, div

argc = len(sys.argv) - 1

if argc != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
    exit(1)

if sys.argv[2] not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

match sys.argv[2]:
    case '+':
        r = a + b
        print("{} + {} = {}".format(a, b, r))
    case '-':
        r = a - b
        print("{} - {} = {}".format(a, b, r))
    case '*':
        r = a * b
        print("{} * {} = {}".format(a, b, r))
    case '/':
        r = a / b
        print("{} / {} = {}".format(a, b, r))
