# This algo is pretty simple. It works with sorted arr and rarely used on practice
# big O of it is O(logN)
# It starts from the very beginning of arr. It jumps on steps and compares elem to arr[step], and twice it on evey step
# If arr[step] is > than elem we make step back and apply a binary search to that interval

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


def exponential_search(arr, element):
    if arr[0] == element:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= element:
        index = index * 2
    return binary_search(arr[:min(index, len(arr))], element)


print(exponential_search([1, 2, 3, 4, 5, 6, 7, 8], 3))
