#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    new = a_dictionary.copy()
    new = new.values()
    new = list(new)
    new.sort(reverse=True)
    maxVal = new[0]
    for i, j in a_dictionary.items():
        if j == maxVal:
            print(i)


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_score(a_dictionary)
