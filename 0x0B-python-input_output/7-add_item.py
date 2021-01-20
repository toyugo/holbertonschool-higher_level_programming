#!/usr/bin/python3
""" Module """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        old = load_from_json_file("add_item.json")
    except:
        old = []
    txt = old + sys.argv[1:]
    save_to_json_file(txt, "add_item.json")
