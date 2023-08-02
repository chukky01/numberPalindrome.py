
def is_palindrome(n):
    """
  This function checks if a number is a palindrome.

  Args:
    n: The number to check.

  Returns:
    True if the number is a palindrome, False otherwise.
  """
    result = 0
    q = n
    
    while q != 0:
        # Get the remainder of the current number divided by 10.
        rem = q%10
        
        # Add the remainder to the reversed number, multiplied by 10.
        result = result*10 +rem
        
        # Divide the current number by 10.
        q = q//10
    # Return true if the reversed number is equal to the original number.
    return result == n
    
    
def main():
    """
  This function prompts the user for a number and then calls the `is_palindrome` function with the number.
  """
    n = int(input("Enter a number and I will tell you if it is a palindrome or not: "))
    
    if is_palindrome(n):
        print("The number entered is a palindrome")
    
    else:
        print("No the number entered is not a palindrome")
    
    
    
if __name__ == "__main__":
    main()
