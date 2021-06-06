def is_palindrome(s):
    def isChars(s):
        s = s.lower()
        s1 = ''
        for x in s:
            if isChars(x):
                s1 = s1 + x
        return s1
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    if isPal(isChars(s)) == True:
        return "YES"
    else:
        return "NO"
