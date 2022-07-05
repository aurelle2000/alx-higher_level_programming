#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding="utf-8") as rf:
        size = rf.readlines()

    with open(filename, 'w', encoding="utf-8") as wf:
        for line in size:
            if search_string in line:
                line += new_string
            wf.write(line)
