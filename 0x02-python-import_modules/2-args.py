#!/usr/bin/python3

if __name__ == "__name__":
    import sys

argc = len(sys.argv)

if argc == 1:
    print(f"{argc - 1} argument.")
elif argc == 2:
    print(f"{argc - 1} argument.")
else:
    print(f"{argc - 1} arguments:")
    for i in range(1, argc):
        print(f"{i}: {sys.argv[i]}")
