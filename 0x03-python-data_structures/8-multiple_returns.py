#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None, 0
    else:
        first_t = sentence[0]
        length_t = len(sentence)

        return length_t, first_t
