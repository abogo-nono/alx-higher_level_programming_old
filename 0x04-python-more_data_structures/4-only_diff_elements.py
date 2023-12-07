#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different = []
    for i, j in zip(set_1, set_2):
        if i not in set_2:
            different.append(i)
        if j not in set_1:
            different.append(j)
    return different
