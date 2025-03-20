#user input
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

#check if divisible by 0
if num2 != 0:
    result = num1 / num2
    print(f"Result: {result}")
else:
    print("Division by zero is not allowed.")
