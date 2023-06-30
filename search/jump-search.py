"""
def jump_search(arr, elem):

    length = len(arr)
    step = int(length**0.5)
    left, right = 0, 0

    while left < length and arr[left] <= elem:
        right = min(length - 1, left + step)

        if arr[left] <= elem <= arr[right]:
            break
        left += step

    if left >= length or arr[left] > elem:
        return -1

    right = min(right, length-1)
    i = left

    while i <= right and arr[i] <= elem:
        if arr[i] == elem:
            return i
        i += 1
    return -1


print(jump_search([1, 2, 3, 4, 5, 6], 5))



def interpolation_search(arr, elem):
    left = 0
    right = (len(arr) - 1)
    while left <= right and arr[left] <= elem <= arr[right]:
        index = left + int(((float(right - left) / (arr[right] - arr[left])) * (elem - arr[left])))
        if arr[index] == elem:
            return index
        if arr[index] < elem:
            left = index + 1
        else:
            right = index - 1
    return -1


print(interpolation_search([1, 2, 3, 4, 5, 6, 7], 4))
"""


def jump_search(arr, elem):
    length = len(arr)
    step = int(length**0.5)
    left, right = 0, 0

    while left < length - 1 and arr[left] <= elem:
        right = min(length - 1, left + step)

        if arr[left] <= elem <= arr[right]:
            break
        left += step

    if left >= length or left >= elem:
        return -1

    right = min(length-1, right)
    i = left

    while i <= right and arr[i] <= elem:
        if arr[i] == elem:
            return i
        i += 1
    return -1


print(jump_search([1, 2, 3, 4, 5, 6, 7], 5))


def interpolation_search(arr, elem):
    left = 0
    right = (len(arr) - 1)

    while left <= right and arr[left] <= elem <= arr[right]:
        index = left + int(((float(right - left) / (arr[right] - arr[left])) * (elem - arr[left])))
        if arr[index] == elem:
            return index
        if arr[index] < elem:
            left = index + 1
        else:
            right = index - 1
    return -1


print(interpolation_search([1, 2, 3, 4, 5, 6, 7, 8], 6))
