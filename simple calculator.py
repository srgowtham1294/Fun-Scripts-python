def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def power(num_1, num_2):
    return num_1 ** num_2

calculator = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power
}

print("""Hey there, I am your calculator. 
      For now I can add,subtract, multiply, divide and give you the power of a number!""")

num_1 = float(input("Please enter your first number: "))

def answer(num_1, num_2, operator):
    return round(calculator[operator](num_1, num_2),1)


is_completed = False

print("What would you like to do?")

for symbol in calculator:
    print(symbol)

while not is_completed:

    operator = input('Enter your option: ')
    num_2 = float(input("Please enter your next number: "))
    if operator not in [symbol for symbol in calculator]:
        print("Please enter a valid option:")
    else:
        final_result = answer(num_1, num_2, operator)
        print(f'The result of {num_1} {operator} {num_2} is {answer(num_1, num_2,operator)}')

    continue_calculation = input("Do you wish to continue? Enter 'y' or 'n': ")

    if continue_calculation == 'y':
        num_1 = final_result
    else:
        print(f"Ending Calculation, Your final result is {final_result}")
        is_completed = True
