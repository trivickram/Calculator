logo="""
_____________________
|  _________________  |
| | 1O           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    print(logo)
    num1 = float(input("Enter First number :"))
    for symbol in operations:
        print(symbol)
    Do_calc = True

    while Do_calc:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_operation = operations[operation]
        result = calc_operation(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result
        else:
            Do_calc = False
            calculator()


calculator()
