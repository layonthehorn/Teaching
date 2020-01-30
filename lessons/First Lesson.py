# imports the best of other peoples work
import random


# functions and when to use them
def random_number_game():
    random_number = random.randint(1, 100) # min 1 max 100
    # what's a bool between friends?
    guessing = True
    # looping around iteration
    while guessing:
        # Taking your response
        p_input = int(input("Guess a number in the range of 1 to 100. "))
        print(random_number)
        # if you're high come down
        if p_input > random_number:
            print("Too high!")
        # if you're low get up
        elif p_input < random_number:
            print("Too low!")
        # if you're right you're right
        else:
            print("You got it!")
            guessing = False


# don't call us, we'll call you
random_number_game()
