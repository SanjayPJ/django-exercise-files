###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
# import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
#
# # Another hint:
# guess = input("What is your guess? ")
# print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!


import random

# GET GUESS

def get_guess():

    return input("What is your guess : ")


# GENERATE COMPUTER CODE 123

def generate_code():

    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    print(digits[:3])
    return digits[:3]

#GENEREATE THE CLUES

def generate_clue( guess , secret_code):

    secret_code_string = ""
    for i in secret_code:
        secret_code_string += i

    if guess == secret_code_string:

        return ("CODE CRACKED")

    clues = []

    for ind,num in enumerate(secret_code):
        if num == guess[ind]:
            clues.append("match")
        elif num in guess:
            clues.append("close")
    if clues == []:
        return ["nope"]
    else:
            return clues

#RUN GAME LOGIC

print("Welcome code breaker!")
secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = generate_clue(guess , secret_code)
    print("Here is the result for your guess : ")
    for clue in clue_report:
        print(clue)
