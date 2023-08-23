# O(N) algorithm

def find_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


print(find_x([1, 2, 4, 2, 5], 2))
