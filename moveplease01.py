#!/usr/bin/env python3
"""Mack | Mackoy Enterprises
    Sample script showing movement of files

    Setup:
    1. mkdir -p ~/mycode/ceph_storage
    2. touch ~/mycode/ceph_storage/kerrigan.obj
    3. touch ~/mycode/raynor.obj

    Clean up:
    1. rm -rf ~/mycode/ceph_storage
    """

# importing standard library modules
import shutil
import os

def main():
    
    """beginning of execution """
    os.chdir('/home/student/mycode/') # start in a working directory
    shutil.move('raynor.obj', 'ceph_storage/') # move file to directory
    
    # prompt for name of destination file
    xname = input('What is the new name for kerrigan.obj? ') # collect input from user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # move existing file
                                                                      # move file prompted to rename

if __name__ == "__main__":
    main()
