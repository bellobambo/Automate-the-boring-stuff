def collatz(number):
    if number % 2 == 0:  # If number is even
        result = number // 2
    else:  # If number is odd
        result = 3 * number + 1

    print(result)
    return result

def collatz_sequence():
    try:
        number = int(input("Enter an integer: "))
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

collatz_sequence()
