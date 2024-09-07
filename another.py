def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations = {
    "+" : add,
    "-" : subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    should_continue = True

    num1 = float(input("Enter the first number: "))
    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol = input("Enter the operation symbol: ")
        num2 = float(input("Enter the second number: "))
        answer = (operations[operation_symbol](num1,num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_choice = input(f"Type 'y' to continue with the {answer} or type 'n' to start a new calculation: ")
        if user_choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" *30)
            calculator()


calculator()


