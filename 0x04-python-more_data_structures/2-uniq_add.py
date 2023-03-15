#!/usr/bin/python3

def uniq_add(my_list=[]):
    int = 0
    for i in set(my_list):
        int += i
    return int
