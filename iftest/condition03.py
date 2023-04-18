#!/usr/bin/env python3
"""Mack | Mackoy Enterprises
    Check entered input against expected value
    """
def main():

    # Collect input from user
    hostname = input("What value should we set for hostname?")
    
    ## Notice how the next line has changed
    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    # Notifying end of code
    print ("Exiting script")

if __name__ == "__main__":
    main()
