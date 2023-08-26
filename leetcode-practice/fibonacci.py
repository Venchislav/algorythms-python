def fib(n):
    if n <= 1:
        return n

    prev1 = 0
    prev2 = 1
    res = 0

    for i in range(1, n):
        res = (prev1 + prev2)
        prev1 = prev2
        prev2 = res
    return res
