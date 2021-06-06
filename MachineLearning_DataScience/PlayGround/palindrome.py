def is_palindrome(s):

    def to_chars(s):
        ans = ''
        for c in s:
            if c.isalpha():
               ans += c
        return ans

    def is_pal(s):
        return s == s[::-1]

    return is_pal(to_chars(s)):

s = input()
if is_palindrome(s):
    print(f'{s} is palindrome')
else:
    print(f'{s} is not palindrome')
