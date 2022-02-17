# problem statement: Write a Python program to find the area and perimeter of a circle. Read inputs from the user.
import math
PI = math.pi
def perimeter(r):
    return 2*PI*r
def area(r):
    return PI*(r**2)
if __name__ == '__main__':
    # x1, y1 = list(map(int, input("Enter the integers:\n").split()))
    n = int(input("Enter the radius for circle:\n"))
    print(f"The area is {area(n)}")
    print(f"The perimeter is {perimeter(n)}")
