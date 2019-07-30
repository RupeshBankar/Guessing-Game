word = input("Please enter a word: ")
reverse_word = word[::-1]
print(reverse_word)

if word == reverse_word:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")