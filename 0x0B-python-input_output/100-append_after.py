#!/usr/bin/python3
""" Module """


def append_after(filename="", search_string="", new_string=""):
    """unction that inserts a line of text to a file,
    after each line containing a specific string"""
    txt = ""
    with open(filename, mode="r") as f:
        for line in f.readlines():
            # print("check :line {} with {}".format(line, line))
            if line in search_string:
                # print("######add new string#####")
                txt = txt + new_string
            else:
                print(False)
                txt = txt + line
    print(txt)
    return (txt)
