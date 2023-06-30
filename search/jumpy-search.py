# Jumpy search (IDK it's real name) is an algo where we jump through the elems with step of sqrt(len)
# We compare if our searched elem is less than that what we got in iterating process
# And if so we go step back and use linear search
# But to use it we have to sort our array first
# Big O for this algo is O(sqrt(N))
# This algo is better than linear but worse than binary one


def jump_search(arr, element):
    length = len(arr)
    step = int(length ** 0.5)
    left, right = 0, 0
    while left < length and arr[left] <= element:
        right = min(length - 1, left + step)
        # Break while loop if our elem is less than the next step elem
        if arr[left] <= element <= arr[right]:
            break
        # if not than add step
        left += step

    # if our elem does not exist in arr
    if left >= length or arr[left] > element:
        return 'Item is not in arr'
    right = min(length - 1, right)
    i = left

    # Simple linear search
    while i <= right and arr[i] <= element:
        if arr[i] == element:
            return i
        i += 1
    return -1


print(jump_search([1, 2, 3, 4, 5, 6, 7], 6))


"""

Explained by ChatGpt:



The code you provided is an implementation of the Jump Search algorithm.
Jump Search is a searching algorithm that works on sorted arrays.
It aims to find the position of a target element in the array efficiently.

Let's go through the code step by step:

def jump_search(arr, element):
   length = len(arr)
   jump = int(math.sqrt(length))
   left, right = 0, 0
   while left < length and arr[left] <= element:
     right = min(length - 1, left + jump)
     if arr[left] <= element and arr[right] >= element:
       break
     left += jump;
   if left >= length or arr[left] > element:
     return -1
   right = min(length - 1, right)
   i = left
   while i <= right and arr[i] <= element:
     if arr[i] == element:
       return i
     i += 1
   return -1


1. The function jump_search takes two parameters: arr (sorted array) and element (the target element we want to find)

2. It initializes the length variable with the length of the array and calculates the jump size
as the square root of the length using the math.sqrt function

3. It initializes the variables left and right to 0.

4. The first while loop is used to find the block in which the target element might be present.
It continues until left is less than the length of the array and the element at left
is less than or equal to the target element.

5. Inside the loop, the right variable is set to the minimum value between length - 1 and left + jump.
This determines the range of the block to be searched.

6. If the element at left is less than or equal to the target element and the element at right is greater
than or equal to the target element, it means the target element is within this block, and the loop is exited.

7. After the loop, if left is greater than or equal to the length of the array or the element at left is greater
than the target element, it means the target element is not present in the array. In this case, the function returns -1.

8. The right variable is updated to the minimum value between length - 1 and right.

9. The variable i is set to left.

10. The second while loop is used to search for the target element within the block determined in the previous steps.
It continues until i is less than or equal to right and the element at i is less than or equal to the target element.

11. Inside the loop, if the element at i is equal to the target element, the function returns the index i.

12. If the target element is not found within the block, the loop continues by incrementing i by 1.

13. If the loop completes without finding the target element, the function returns -1.

Overall, the code implements the Jump Search algorithm to search for a target element in a sorted array.
It uses the concept of blocks and jumps to efficiently narrow down the search range.
"""


# P.S Damn, this bro is smarter than me
