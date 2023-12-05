#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    else:
        print("Length: {} - First character:{}".format(len(sentence), sentence[0]))
