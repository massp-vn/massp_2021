def palindrome(s):
    return (s == s[::-1])
s = input("Enter the string : ")
ans = palindrome(s)
if ans == 1: 
	print(s, "is a Palindrome")
else: 
	print(s, "is not a Palindrome")
