"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    high=max(incoming_list)
    return high


def find_least_number(incoming_list):
    low=min(incoming_list)
    return low


def add_list_numbers(incoming_list):
    total=sum(incoming_list)
    return total


def longest_value_key(incoming_dict):
    longest=max(len(i) for i in incoming_dict)
    return longest
