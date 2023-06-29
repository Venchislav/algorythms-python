# This algo works only with sorted arrs
# It tries to guess index
# It has a formula index = A + ((F - arr[A] * (B - A)) / (arr[B] - arr[A]) where F iss elem we search for
# A,B - bounds for searched elem S
# And if F != index: if F > arr[index] (search in right part with the same algo) F < arr[index] (search in left part)
# Big O for this algo is O(logN)
# This algo is used for arrs with uniform data


def interpolation_search(arr, element):
    left = 0
    right = (len(arr) - 1)
    while left <= right and arr[left] <= element <= arr[right]:
        index = left + int(((float(right - left) / (arr[right] - arr[left])) * (element - arr[left])))
        if arr[index] == element:
            return index
        if arr[index] < element:
            left = index + 1
        else:
            right = index - 1
    return -1


print(interpolation_search([1, 2, 3, 4, 5, 6, 7], 5))

# Well it's pretty easy algo... And it's very similar to binary_search
