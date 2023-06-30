# IMHO Bubble Sort is the worst piece of sh1t as it has O(N * N)
# The only advantage of it is it's easy realisation
# So it's only used for little arrs


def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort([6, 5, 3, 4, 1, 2]))
