def find_max2(seq):
    # setting fist 2 elems as max
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])

    for i in range(len(seq)):
        # if elem is bigger than max1 and max2 (logical as max2 is less than max1)
        if seq[i] > max1:
            # replace values. max1 with elem and max2 with max1
            max2 = max1
            max1 = seq[i]
        # else if elem is bigger than max2 but less than max1 (possible)
        elif seq[i] > max2:
            # replace max2 with elem
            max2 = seq[i]

    return max1, max2


print(find_max2([1, 2, 3, 4, 5, 6, 7]))
