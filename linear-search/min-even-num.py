def find_min_even(seq):
    flag = False
    minimum = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < minimum):
            minimum = seq[i]
            flag = True
    return minimum


print(find_min_even([1, 2, 3, 4, 5, -10]))
