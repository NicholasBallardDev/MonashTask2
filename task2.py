import random

'''
    A game where the user will have to guess a randomly selected number from 1-100
    With each guess feedback will be given: "higher", "lower" or "correct"
    When the user guesses correctly the game ends 
'''

#Checks whether the user input is higher, lower or on the target number using if statements
#Returns values accordingly
def check_answer(num, target):
    #if num is more than target
    if num > target:
        return "lower"
    #less than
    elif num < target:
        return "higher"
    #equal to target
    else:
        return "correct"

#Checks whether the user input is valid by checking the user input to a list of valid inputs
def is_valid(user_input):
    #Creates a list: ["1","2","3"..."100"]
    valid_inputs = [str(i) for i in range(1,101)]

    #Returns true if the user input is between 1 and 100
    if user_input in valid_inputs:
        return True
    #Otherwise return False
    else:
        return False

def run_game():
    #Chooses target as a random number from 1-100
    target = random.randint(1,100)

    #Infinitely loops through until the user guesses correctly
    while True:
        user_input = input("Enter an integer between 1 and 100: ")
        #Checks for a valid input
        if is_valid(user_input):
            #Checks if the answer is correct
            res = check_answer(int(user_input), target)
            print(res)
            #Ends the game if the guess is correct
            if res == "correct":
                return  
        #If the input is invalid, an error message displays
        else: 
            print("Invalid input, please enter an integer between 1 and 100 instead")


#Code to run the game
run_game()





