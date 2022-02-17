# problem statement: 
# Write a Python program to calculate the compound interest based on the given formula. Read inputs
# from the user. A = P * (1 + R/100)^T where P is the principle amount, R is the interest rate and T is time (in years).

def compound_interest_2019_1_60_136(P,R,T):
    return P*((1+(R/100))**T)
if __name__ == '__main__':
    P = int(input("Enter Principle amount:\n"))
    R = int(input("Enter Rate of interest:\n"))
    T = int(input("Enter time:\n"))

    A = compound_interest_2019_1_60_136(P, R, T)
    print(f"The compound interest:\n{A} ")

# test:
# Enter Principle amount:
# 145
# Enter Rate of interest:
# 2
# Enter time:
# 1
# The compound interest:
# 147.9