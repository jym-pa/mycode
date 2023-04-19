#!/usr/bin/env python3
"""
Mack | Mackoy Enterprises
Get a synopsis of a book using if-logic
Inspired by https://stackoverflow.com/a/70089051
"""

def main():

    movie = {
    "Harry Potter (first one)": "You're a wizard, Harry!",
    "Hobbit & Lord of the Rings": "One ring to rule them all ...",
    "Chronicles of Narnia": "Liam Neeson is a lion!",
    "Indiana Jones": "He hates snakes.",
    }

#    for c, desc in movie.items():
#        print(f"{c}. {desc}")

    choice = input("Press Enter to see movie synopsis selections ...")
    while choice not in movie:
        choice = input(f"Choose one of: {', '.join(movie)}: ")
    
    print(f"Synopsis: {movie[choice]}")
    
if __name__ == "__main__":
    main()

