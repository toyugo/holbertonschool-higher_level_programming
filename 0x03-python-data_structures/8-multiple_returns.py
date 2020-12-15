#!/usr/bin/python3/
def multiple_returns(sentence):
    if sentence is None:
        return None
    lenght = len(sentence)
    firstchar = sentence[0]
    return lenght, firstchar
