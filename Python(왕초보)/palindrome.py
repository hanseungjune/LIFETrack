def palindrome(text):
    if text.replace(' ', '').lower() == text[::-1].replace(' ', '').lower():
        return True
    else:
        return False

print(palindrome('A   nn    a'))
print(palindrome('b a na  na'))