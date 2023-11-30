#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if (i != j):
            print(f"{(i * 10 +j):02d}", end='')
            if (i * 10 +j != 89):
                print(', ', end='')
            else:
                print('\n', end='')
