#!/bin/usr/python3

def remove_char_at(str, n):
    s2 = ""
    for i in range(0, len(str)):
        if i != n:
            s2 += str[i]
    return s2
