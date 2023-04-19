#!/usr/bin/env python3
"""
Mack | Mackoy Enterprises
while statement practice in the context of Monty Python
"""

round = 0  # setting the round counter value to zero, to start

while True:  # start an infinite loop condition
    round = round + 1  # increase round counter by one
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")  # collect answer from user as string
    if answer == 'Brian':  # checking to see if user gave correct answer
        print('Correct')
        break  # break point to escape the while loop
    elif round==3:  # if we get to the point where three false guesses are given
        print("Sorry, the answer was Brian.")
        break  # break point to escape the while loop
    else:  # if the answer is incorrect, but haven't given three guesses already
        print("Sorry! Try again!")

