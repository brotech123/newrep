def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

def main():
    # Get input from user
    num = int(input("Enter a positive integer to calculate its factorial: "))
    
    # Check if the number is negative
    if num < 0:
        print("Factorial cannot be calculated for negative numbers.")
        return
        
    # Calculate and display the result
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

main()
