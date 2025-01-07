def calculator_program(input1, input2, operation_input):
    if operation_input == "+":
        print(f"{input1 + input2} \n")
    elif operation_input == "/":
        print(f"{input1 / input2} \n")
    elif operation_input == "*":
        print(f"{input1 * input2} \n")
    elif operation_input == "-":
        print(f"{input1 - input2} \n")
    else:
        return "Invalid input!"

calculation_counter = 0

while True:
    first_input = input("Number 1 (or type 'exit' to quit): ")

    if first_input.lower() == "exit":
        print(f"Thanks for using our calculator! Total calculations: {calculation_counter}")
        break

    try:
        number1 = int(first_input)
    except ValueError:
        print("That is not a number! \n")
        continue

    operation = input("Enter an operation (+, -, *, /): ")
    valid_operations = ['+', '-', '/', '*']

    if operation not in valid_operations:
        print("Invalid operation! \n")
        continue

    try:
        number2 = int(input("Number 2: "))
    except ValueError:
        print("That is not a number! \n")
        continue

    calculator_program(number1, number2, operation)
    calculation_counter += 1

