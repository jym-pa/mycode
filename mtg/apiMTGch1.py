#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests
import json
import pprint

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup

    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = resp.json()
    
    # Showing cards output
    print("Showing raw output from cards in json")
    print(cards)
    print("Showing prettyprinter output")
    pretty_cards = pprint.pprint(cards)
    print(pretty_cards)


    # Writing cards output to file - stupid API responds once out of 20 times
    with open (f"mtgcardfile_{setcode}.json", "w") as json_mtgcardfile:
        json_mtgcardfile.write(str(cards))
        json_mtgcardfile.close()

    with open (f"pretty_mtgcardfile_{setcode}.json", "w") as pretty_json_mtgcardfile:
        pretty_json_mtgcardfile.write(str(pretty_cards))
        pretty_json_mtgcardfile.close()

#    TODO: Parse json_mtgcardfile using json.load
#          After that, same logic should be usable on data from the API call - resp

#    # Load the cards output into a json object
#    card_data = json.load(cards)
#
#    # open a file to write data into
#    print(f"Writing formatted subset of data to mtgcards_set{setcode}.index:")
#    with open(f"mtgcards_set{setcode}.index", "w") as mgtcardfile:
#        # Using the json object, iterate through
#        for card in card_data['cards']:
#            print(f"{card.get('name')} -- {card.get('type')} -- {card.get('rarity')}", file=mgtcardfile)


if __name__ == "__main__":
    main()

