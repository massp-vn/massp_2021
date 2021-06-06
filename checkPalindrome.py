###Given a string, write a python function to check if it is palindrome or not. 
#A string is said to be palindrome if the reverse of the string is the same as string. 
#For example, “radar” is a palindrome, but “radix” is not a palindrome.

def checkPalindrome(s):
    length = len(s)
    i = 0
    while i < length/2: 
        if s[i] != s[length-i-1]:
           return False
        i += 1
    return True
print(checkPalindrome("radix"))
print(checkPalindrome("radar"))