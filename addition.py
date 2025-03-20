def add(x, y):
    return x + y

def main():
    print("Welcome to the CLI Calculator!")
    
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing addition
        result = add(num1, num2)

        # Displaying the result
        print(f"The result of {num1} + {num2} is: {result}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    
if __name__ == "__main__":
    main()
