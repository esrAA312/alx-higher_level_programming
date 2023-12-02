#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    first_char = sentence[0] if l > 0 else "None"
    tup = l, first_char
    return (tup)
