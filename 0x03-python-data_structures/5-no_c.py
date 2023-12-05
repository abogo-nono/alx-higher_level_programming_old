def no_c(my_string):
    new_string = ''
    for i in my_string:
        new_string += "" if i == 'C' or i == 'c' else i
    return str(new_string)
