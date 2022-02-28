# problem statement: Given a two list of numbers (hardcoded in the program), create a new list such that new list should
# contain only odd numbers from the first list and even numbers from the second list.

def odd_even_merger(od,ev):
    i = 0
    j = 0
    sol = []
    while i<len(od) and j<len(ev):
        if od[i] % 2 == 1:
            sol.append(od[i])
        i += 1
        if ev[j] % 2 == 0:
            sol.append(ev[j])
        j += 1
    while i<len(od):
        if od[i] % 2 == 1:
            sol.append(od[i])
        i += 1
    while j<len(ev):
        if ev[j] % 2 == 0:
            sol.append(ev[j])
        j += 1
    return sol



if __name__ == '__main__':
    first_list = [12, 17, 20, 13]
    second_list = [6, 9, 4, 5, 2]

    print(f"The merged list is:{odd_even_merger(first_list, second_list)}")

# test:
# The merged list is:[6, 17, 4, 13, 2]
