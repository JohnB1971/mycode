#!/usr/bin/env python3

# add counter
round = 0

# add loop to the program that will require a break.
while True:

# add in counter to kill the program after a certain number of tries.

    round = round + 1
# Ask the question
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
# Wait for response from player    
    answer = input("Your guess--> ")
# Check if answer is correct.    
    if answer == 'Brian':
        print('Correct')
# End the loop if correct       
        break
# If incorrect see if maximum number of chances have been reached, end the loop.
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
# Print try again message.
    else:
        print("Sorry! Try again!")

