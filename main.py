last_value = None

def outer_function():
    global last_value

    def add_number(first, second):
        return first + second

    def subtract_number(first, second):
        return first - second

    def multiply(first, second):
        return first * second

    def divide(first, second):
        if second == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return first / second


    first_number = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    second_number = float(input("Enter second number: "))

    if operation == "+":
        last_value = add_number(first_number, second_number)
        print(f"{first_number} + {second_number} = {last_value}")
    elif operation == "-":
        last_value = subtract_number(first_number, second_number)
        print(f"{first_number} - {second_number} = {last_value}")
    elif operation == "*":
        last_value = multiply(first_number, second_number)
        print(f"{first_number} * {second_number} = {last_value}")
    elif operation == "/":
        last_value = divide(first_number, second_number)
        print(f"{first_number} / {second_number} = {last_value}")
    else:
        print("Invalid operation")
        return

    while True:
        continue_calculation = input("Would you like to continue? (y/n): ")
        if continue_calculation.lower() == "y":
            first_number = last_value
            operation = input("Enter operation (+, -, *, /): ")
            second_number = float(input("Enter second number: "))
            if operation == "+":
                last_value = add_number(last_value, second_number)
                print(f"{last_value - second_number} + {second_number} = {last_value}")
            elif operation == "-":
                last_value = subtract_number(last_value, second_number)
                print(f"{last_value + second_number} - {second_number} = {last_value}")
            elif operation == "*":
                last_value = multiply(last_value, second_number)
                print(f"{last_value / second_number} * {second_number} = {last_value}")
            elif operation == "/":
                last_value = divide(last_value, second_number)
                print(f"{last_value * second_number} / {second_number} = {last_value}")
            else:
                print("Invalid operation")
        else:
            print(f"Final Result = {last_value}")
            break
outer_function()