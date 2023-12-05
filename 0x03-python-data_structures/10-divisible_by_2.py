#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    my_result = []
    for i in my_list:
        if (i % 2) == 0:
            my_result.append(True)
        else:
            my_result.append(False)
    return my_result
