# problem statement: Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
# built-in function.

def find_occurences(s,r):
    win_len = len(r)
    i = 0
    j = win_len - 1
    count = 0
    while j<len(s):
        x, y = i, j
        stri = ''
        while x<=y:
            stri += s[x]
            x += 1
        if stri == r:
            count += 1
        i += 1
        j += 1
    return count


    return count
if __name__ == '__main__':
    s = input("Enter the string:\n")
    r = 'CSE303'
    print(f"{find_occurences(s,r)} number of occurences are found")

# test:
# CSE303 is the best course. We all should take CSE303. The cost of CSE303 is 4900/cr
# 3 number of occurences are found

