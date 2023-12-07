#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.items())
    for i, j in sorted_list:
        print('{}: {}'.format(i, j))
