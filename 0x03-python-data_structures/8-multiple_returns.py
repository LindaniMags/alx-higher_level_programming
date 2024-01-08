#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_ = ()
    if len(sentence) == 0:
        tuple_ = 0, "None"
    else:
        tuple_ = len(sentence), sentence[0]
    return tuple_
