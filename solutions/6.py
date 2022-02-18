# problem statement: Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
# number based on the following assumptions.

def fib(n):
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)
if __name__ == '__main__':
    n = int(input("Enter a positive number:\n"))
    print(f"{n}th fibonacci term : {fib(n)}")

# test:
# 5th fibonacci term : 8