# Specify a dummy number
dummy_number = int(input("enter a number"))

# Use ternary operator to check if the number is even or odd
result = "even" if dummy_number % 2 == 0 else "odd"

# Display the result
print(f"The number {dummy_number} is {result}.")
