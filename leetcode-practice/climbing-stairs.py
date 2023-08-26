def stairs(n):
    if n <= 2:
        return n

    prev1 = 1
    prev2 = 2
    res = 0

    for i in range(2, n):
        res = (prev1 + prev2)
        prev1 = prev2
        prev2 = res
    return res


print(stairs(4))
