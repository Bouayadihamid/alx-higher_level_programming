#!/usr/bin/python3
for num in range(10):
    for i in range(10):
        if num < i:
            if num == 8 and i == 9 else ", "
            print("{:d}{:d}".format(num, i), end="")
print()
