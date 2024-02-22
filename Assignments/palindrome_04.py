"""
Assignment4

"""

input_word = input("Enter a word to check if it's palindrome :")

Rev_word = input_word[::-1]

print("Given word : {} \nReversed word : {}".format(input_word, Rev_word) )

if input_word == Rev_word:
    print(input_word, " is a palindrome" )
else:
    print(input_word, " is not a palindrome" )
