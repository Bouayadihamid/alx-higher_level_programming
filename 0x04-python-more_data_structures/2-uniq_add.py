#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set()
    for i in my_list:
        if i not in uniq_set:
            uniq_set.add(i)
    uniq_sum = sum(uniq_set)
    return uniq_sum
