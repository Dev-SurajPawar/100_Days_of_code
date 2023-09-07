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


def calculate():
    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print('(', symbol, ')', end=" ")

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation form above: ")
        num2 = float(input("What's the next number: "))
        calculate_function = operations[operation_symbol]
        ans = calculate_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {ans}")

        if input(f"Type 'Y' to continue calculate with {ans}, or type 'N' to start a new calculation: ").upper() == "Y":
            num1 = ans
        else:
            should_continue = False
            calculate()


calculate()
