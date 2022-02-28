# problem statement:
# Given a positive integer N (read from the user), write a Python program to check if the number is
# prime or not. Define a function named as prime_find_<your-student-id> in your program.
def is_prime(n):
    if n < 3 and not n == 2:
        if n == 2:
            return "prime"
        else:
            return "not prime"

    for i in range(2,n):
        if n % i == 0:
            return "not prime"
    return "prime"
        
if __name__ == '__main__':
    N = int(input("Enter number to check\n"))
    print(f"{N} is {is_prime(N)}")

# test:
# 459
# 459 is not prime