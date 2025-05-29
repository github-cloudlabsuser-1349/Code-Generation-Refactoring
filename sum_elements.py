# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    return sum(numbers)

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ")
        if not 1 <= n <= MAX_ELEMENTS:
            print(f"Invalid input. Please provide a number between 1 and {MAX_ELEMENTS}.")
            return

        numbers = []
        for i in range(n):
            num = get_integer(f"Enter integer #{i+1}: ")
            numbers.append(num)

        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
