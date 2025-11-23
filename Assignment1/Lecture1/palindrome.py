def check_palindrome(s):
    return is_palindrome(s, 0, len(s)-1)


def is_palindrome(s, first, last):
    if first >= last:
        return True
    if s[first] != s[last]:
        return False
    return is_palindrome(s, first+1, last-1)


print(check_palindrome(''))
print(check_palindrome('x'))
print(check_palindrome('anna'))
print(check_palindrome('madam'))
print(check_palindrome('abcdefedcba'))
print(check_palindrome('yyyyyyyy'))

print(check_palindrome('Tharanga'))
