#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}

    for i in list(a_dictionary.keys()):
        new_dic[i] = a_dictionary[i] * 2

    return new_dic