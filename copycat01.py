#!/usr/bin/env python3
"""Mack | Mackoy Enterprises
   Playing around with the filesystem"""

# import additional modules for our, eh, module
import shutil
import os


def main():
    """begin code to move around files"""

    # move cursor into working directory
    os.chdir("/home/student/mycode/")
    
    # copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    # copy whole directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
