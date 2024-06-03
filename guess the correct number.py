import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def choose_level():
    level = input("Please choose your level, easy or hard? :")
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS

chosen_number = random.randint(1,100)

def number_game():

    attempts = choose_level()
    is_game_finished = False

    while not is_game_finished and attempts>0:
        user_input = int(input(f"You have {attempts} attempts left. Please enter your guess: " ))
        if user_input < chosen_number:
            attempts = attempts -1
            print(f"The number you chose is too small. You have {attempts} attempts left. Pick again")
        elif user_input > chosen_number:
            attempts = attempts - 1
            print(f"The number you chose is too large. You have {attempts} attempts left. Pick again")
        elif user_input == chosen_number:
            print("Congratulations, you've chosen the correct number!")
            is_game_finished = True
        
        if attempts==0:
            print("Sorry, You've exhaused your chances! You lost!")
            is_game_finished = True

number_game()





