#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l > 0:
        c = sentence[0]
    else:
        c = None
    t = l, c

    return t
