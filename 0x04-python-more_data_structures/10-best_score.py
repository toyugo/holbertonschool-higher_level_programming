#!/usr/bin/python3/
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    new = a_dictionary.copy()
    new = new.values()
    new.sort(reverse=True)
    if new[0]:
        return new[0]
