def tribonacci(n):
    if n == 2 or n == 1:
        return 1

    prev1 = 0
    prev2 = 1
    prev3 = 1
    res = 0

    for i in range(2, n):
        res = (prev1 + prev2 + prev3)
        prev1 = prev2
        prev2 = prev3
        prev3 = res
    return res
