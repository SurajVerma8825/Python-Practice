def palindrome(word):
    if word == word[::-1]:
        return "It is a palindrome"
    else:
        return "Not a palindrome"

word = input("Please enter the word: ")

print(palindrome(word))
