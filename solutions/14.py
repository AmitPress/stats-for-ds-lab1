# problem statement: Given a string, write a python program to check if it is palindrome or not. Define a function named
# palindrome_checker_<your-student-id> in your program.
def palindrome_checker_2019_1_60_136(s):
    is_palindrome = False
    i = 0
    j = len(s)-1
    rev_str = ''
    while j>=i:
        rev_str += s[j]
        j -= 1
    if rev_str == s:
        is_palindrome = True
    return is_palindrome
if __name__ == '__main__':
    s = input("Enter the string to check:\n")
    if palindrome_checker_2019_1_60_136(s):
        print("The string is Palindrome")
    else:
        print("The string is not Palindrome")

# test:
# Enter the string to check:
# madam
# The string is Palindrome
# Enter the string to check:
# madame
# The string is not Palindrome
    