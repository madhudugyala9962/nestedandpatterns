# Create a Python program that prints a simple number pattern (e.g., square, triangle, or diamond) using nested loops.
# Implement a function that takes an integer input from the user and generates the pattern based on the input size.
# Use conditional statements to handle invalid input (e.g., non-integer or negative numbers).
# Ensure the program includes proper error handling and provides user-friendly feedback.
# Submit the Python source code file (.py) with a clear and descriptive filename.
for x in range(1, 6):
    for y in range(1, 6):
        if x==1 or y==1 or x==5 or y==5:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()