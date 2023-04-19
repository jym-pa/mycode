#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching

EXCLUDE = ["/usr", "/home", "/var", "/snap"] ## Don't search in these locations


def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        print("Here are the files found:")
        print(files)
        print("Here is the lowercase version of those files:")
        lower_files = [x.lower() for x in files]
        print(lower_files)
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in lower_files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def main():
    """runtime code"""
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    print("Here is the pattern entered:")
    print(lookfor)
    print("Here is the case insensitive (lowered) version:")
    lower_lookfor = lookfor.lower()
    print(lower_lookfor)

    lookwhere = input("What is the path in which I should search? ")

    print("Results: ", find(lower_lookfor, lookwhere)) # call function

main()

