def palindrome(word):
    # Base case
    if len(word) <= 1:
        return True
    else: # General case
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False
print(palindrome("Bayu"))
