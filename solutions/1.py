# problem statement: Given two integer numbers, write a Python program to return their product. If the product is greater
# than 1000, then return their sum. Read inputs from the user.

# let x & y be the given two integers

def solution(x,y):
    product = x*y 
    if product>1000:
        return x+y 
    else:
        return product
    
if __name__ == '__main__':
    x1, y1 = list(map(int, input("Enter the integers:\n").split()))
    print(solution(x1,y1))

# tests:
# λ py 1.py
# Enter the integers:
# 455 4
# 459