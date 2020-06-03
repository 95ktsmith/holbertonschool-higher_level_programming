#!/usr/bin/python3
""" Arguments to json file """
import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    """ Load object from add_item.json, add arguments to it, save into file """
    try:
        my_list = load_from_json_file("add_item.json")
    except:
        my_list = []
    for index in range(1, len(sys.argv)):
        my_list.append(sys.argv[index])
    save_to_json_file(my_list, "add_item.json")
