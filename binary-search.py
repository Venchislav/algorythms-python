def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right and (index == -1):
        mid = (left + right) // 2
        if arr[mid] == elem:
            index = mid
        else:
            if elem < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return index


print(binary_search([1, 2, 3, 4, 5, 6], 4))
