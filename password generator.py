import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
             'P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['@','#','$','&','*','?','+','-','=']

password_list = []

def get_length():
    password_length = int(
    input("How long do you want your password to be? Minimum length by default will be 6: "))
    
    if password_length < 6:
        print("The length you entered is too short. Hence proceeding with default of 6 characters. ")
        return 6
    else:
        return password_length

def generate_password():

    password_length = get_length()

    alphabets_count = round(password_length*.60)

    numbers_count = round(password_length*.20)

    symbols_count = round(password_length*.20)

    for char in range(0, alphabets_count):
        password_list.append(random.choice(alphabets))

    for num in range(0, numbers_count):
        password_list.append(random.choice(numbers))

    for symbol in range(0, symbols_count):
        password_list.append(random.choice(symbols))

    # print(password_length, alphabets_count, numbers_count, symbols_count)

    # print(password_list)

    random.shuffle(password_list)

    password = "".join([str(i) for i in password_list])

    return password

print(f"The password generated for you is {generate_password()}")

