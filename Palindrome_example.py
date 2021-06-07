#Function 
def palindrome(str):
    for i in range(0, int(len(str) / 2), 1):
        if str[i] != str[len(str) - i - 1]:
            return False
        else:
                return True
    return True

# The main to test
s = "hannah"
case = palindrome(s)
if (case):
    print("The word is palindrome")
else:
    print("The word is not palindrome")