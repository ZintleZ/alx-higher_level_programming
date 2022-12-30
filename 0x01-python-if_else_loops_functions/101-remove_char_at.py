#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or len(str) < n:
        return str
    char = str[n]
    return str.replace(char, "")
