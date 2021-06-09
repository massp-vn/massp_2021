#Function 
def palindrome(str):
    if (str==str[::-1]):
        return True
    return False

# The main to test
s=input()
case = palindrome(s)
if (case):
    print("The word is palindrome")
else:
    print("The word is not palindrome")