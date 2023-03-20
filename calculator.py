import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Calculator
#Add


def add(n1, n2):
    return n1 + n2

#Substract

def substract(n1, n2):
    return n1 -n2

#Multiply

def multiply(n1, n2):
    return n1 * n2
#Divide

def divide(n1, n2):
    if n2 == 0:
        return "No division"
    return n1 / n2

operations = {"+": add, "-": substract, "*":multiply, "/":divide,}

def calculator():
    num1 = float(input("Whats the first number#?\n"))


    for key in operations:
        print(key)

    operations_symbol = input("pick an operaion from above:\n")
    calculation_function = operations[operations_symbol]
    num2 = float(input("Whats the second number#?\n"))

    answer = calculation_function(num1, num2)


    print(f"{num1} {operations_symbol} {num2} = {answer}")


    next_number = False

    while not next_number:

        add_number = input("Weitermachen? 'restart', 'Yes' or 'No\n")
        if add_number.lower() == "no":
            print("berechnung abgeschlossen")
            next_number = True
        elif add_number.lower() == "restart":

            calculator()
        else:
            answerX = answer

            for key in operations:
                print(key)
            operations_symbol = input("pick an operaion from above:\n")
            calculation_function = operations[operations_symbol]
            numX = float(input("Whats the nextnumber#?\n"))
            answer = calculation_function(answerX, numX)


            print(f"{answerX} {operations_symbol} {numX} = {answer}")


calculator()
