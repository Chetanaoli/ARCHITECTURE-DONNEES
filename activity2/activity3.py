def add_two_numbers():
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        print("Invalid input. Please enter valid integer numbers.")
        return

    result = num1 + num2
    return result
