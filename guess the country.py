import random

print("Welcome to the word guessing name. \n")

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z',' ']

words_list = ['amsterdam', 'india', 'netherlands', 'australia', 'united kingdom']

EASY_LEVEL_ATTEMPTS = 20
HARD_LEVEL_ATTEMPTS = 10

def check_level():
    level = input("Enter your level, 'easy' or 'hard'? :")
    if level =='easy':
        print(f'You will get {EASY_LEVEL_ATTEMPTS} attempts!')
        return EASY_LEVEL_ATTEMPTS
    elif level == 'hard':
        print(f'You will get {HARD_LEVEL_ATTEMPTS} attempts!')
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Enter a proper level!")
        return check_level()

chosen_word = random.choice(words_list)
word_length = len(chosen_word)
attempts = check_level()

# print(chosen_word)
display = []

print("Guess the letter: ")

for i in chosen_word:
    display.append('_')

print(display)

end_of_game = False

while not end_of_game:
    user_input = input('Enter your first guess, if multiple characters are entered, only the first character will be considered: ').lower()[0]

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == user_input:
            display[position] = letter
        
    if user_input not in chosen_word:
        attempts -= 1
        if attempts == 0:
            print("You lost all your attempts. Try again!")
            end_of_game = True
        else:
            print(f"You lost a life! You have {attempts} attempts left!")
    
    print(display)

    if '_' not in display:
        print(f"You win! The answer is {''.join(str(i) for i in display)}")
        end_of_game = True
