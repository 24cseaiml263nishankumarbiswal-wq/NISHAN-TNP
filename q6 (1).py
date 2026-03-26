#Check if a string is a palindrome.

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")