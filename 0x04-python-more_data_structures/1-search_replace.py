#!/usr/bin/python3

def search_element(my_list, search, replace):
    def find_element(element):
        return element if element != search else replace
    return list(map(find_search, my_list))
