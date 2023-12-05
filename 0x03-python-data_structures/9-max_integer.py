#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        biggest = my_list[0]
        for i in my_list:
            biggest = i if i > biggest else biggest
        return biggest
    else:
        return None
