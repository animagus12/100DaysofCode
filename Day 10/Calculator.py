from art import logo

# Addition
def add(n1, n2):
    return n1 + n2

# Substraction
def sub(n1, n2):
    return n1 - n2

# Multiplication
def mul(n1, n2):
    return n1 * n2

# Division
def div(n1, n2):
    return n1 / n2

global operations
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div, 
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    rerun = "y"
    while (rerun != "n"):
        for operands in operations:
            print(operands)
        operation_choice = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        print(f"{num1} {operation_choice} {num2} = {operations[operation_choice](num1, num2)}")
        num1 = operations[operation_choice](num1, num2)
        rerun = input("Type 'y' to continue calculating, or type 'n' to start a new calculation.: ")
    calculator()    
calculator() 