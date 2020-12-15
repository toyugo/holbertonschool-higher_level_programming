#!/usr/bin/python3/
def multiple_returns(sentence):
    if len(sentence) is None:
        firstchar = None
    else:
        firstchar = sentence[0]
    lenght = len(sentence)
    return lenght, firstchar
