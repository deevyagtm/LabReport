s = input("Enter a string: ")
if all(char.isalpha() or char.isspace() for char in s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
else:
    print("Error: Please enter only letters.")