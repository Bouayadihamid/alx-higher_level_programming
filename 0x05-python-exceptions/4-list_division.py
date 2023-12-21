#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    NewList = []

    for i in range(list_length):
        try:
            NewList.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            NewList.append(0)
            print("division by 0")
            continue
        except IndexError:
            NewList.append(0)
            print("out of range")
            continue
        except TypeError:
            NewList.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return NewList
