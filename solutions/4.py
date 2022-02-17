# problem statement:
# Given a positive integer N (read from the user), write a Python program to calculate the value of the
# following series. 1^2+2^2+3^2+...+N^2
def solution(n):
    if n==1:
        return 1
    return n**2+solution(n-1)
if __name__ == '__main__':
    n = int(input("Enter positive integer:\n"))
    for i in range(n):
        if not i==n-1:
            print(f"{i+1}^2+",end="")
        else:
            print(f"{i+1}^2",end="")
    print(f"={solution(n)}")

# test:
# 1^2+2^2+3^2+4^2+5^2+6^2=91 
