def palindrome_check(inp_str):
    if inp_str == inp_str[::-1]:
        return True
    else:
        return False


input_string = input()
if palindrome_check(input_string):
    print("'"+input_string+"'"+" is a palindrome")
else:
    print("'"+input_string+"'"+" is not a palindrome")
