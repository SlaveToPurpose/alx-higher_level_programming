#!/usr/bin/python3
def multiple_returns(sentence):
    tup_vala = len(sentence)
    if sentence == "":
        tup_valb = None
    else:
        tup_valb = sentence[0]
    return (tup_vala, tup_valb)
