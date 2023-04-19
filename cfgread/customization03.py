#!/usr/bin/env python3

# total the number of lines in a file by adding + 1 for each line
num_lines = sum(1 for line in open("vlanconfig.cfg", "r"))
# share with the class
print(num_lines)

