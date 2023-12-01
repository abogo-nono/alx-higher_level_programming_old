#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argc = len(sys.argv)

s = 0

for i in range(1, argc):
    s += int(sys.argv[i])

print("{}".format(s))
