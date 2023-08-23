def biggest_in_seq(seq):
    try:
        maximum = seq[0]
    except IndexError:
        return -1

    for item in seq[1:]:
        if item > maximum:
            maximum = item
    return maximum


print(biggest_in_seq([1, 2, 3, 4, 5, 6, 7]))
