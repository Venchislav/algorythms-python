# sel_ssort is slow too O(N * N), but it works faster as it makes fewer moves of elems
# It is also used only with little arrays

def sel_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
