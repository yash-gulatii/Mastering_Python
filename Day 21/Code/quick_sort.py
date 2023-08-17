"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):

    if len(array) < 2:
        return array
    
    pivot = array[0]

    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]

    left_array = quicksort(left)
    right_array = quicksort(right)

    sorted_array = left_array + [pivot] + right_array

    return sorted_array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))