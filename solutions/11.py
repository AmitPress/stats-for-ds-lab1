# problem statement: Given a string, display only those characters which are present at an even index number. Read inputs
# from the user.

def solution(s):
    for i, c in enumerate(s):
        if i%2 == 0:
            print(c,end=" ")
if __name__ == '__main__':
    s = input("Enter the string:\n")
    solution(s)

# test:
# I love string
# 0123456789012
# I l v   t i g