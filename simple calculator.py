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

calculation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power
}

def calculator():
    print('\n\n')
    print("""Hey there, I am your calculator. 
        For now I can add,subtract, multiply, divide and give you the power of a number!""")

    num_1 = float(input("Please enter your first number: "))

    def answer(num_1, num_2, operator):
        return round(calculation[operator](num_1, num_2),1)

    is_completed = False

    while not is_completed:

        print("What would you like to do?")
        
        for symbol in calculation:
            print(symbol)

        operator = input('Enter your option: ')

        num_2 = float(input("Please enter your next number: "))
        if operator not in [symbol for symbol in calculation]:
            print("Please enter a valid option:")
        else:
            final_result = answer(num_1, num_2, operator)
            print(f'The result of {num_1} {operator} {num_2} is {final_result}')

        continue_calculation = input("Do you wish to continue? Enter 'y' for yes, 'n' for new calculation or 'e' for exit: ")

        if continue_calculation == 'y':
            num_1 = final_result
        elif continue_calculation == 'e':
            print(f"Ending Calculation, Your final result is {final_result}")
            is_completed = True
        elif continue_calculation == 'n':
            print('\n\nResetting calculator!')
            calculator()
        else:
            print(f"You entered a wrong input. Your final result is {final_result}.")
            print("Closing the application")
            is_completed = True

calculator()
