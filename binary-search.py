"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Quickly search if a value is present in an array. Returns the index of value, or -1 if the value is not present in the list."""
    len_array = len(input_array)
    if len_array == 0:
        return -1
    #if len_array == 1:
    #    return 0 if value == input_array[0] else -1
    array_mid, remainder = divmod(len_array, 2)
    #array_mid = len_array // 2
    current_index = array_mid if remainder == 1 else array_mid - 1
    current_elem = input_array[current_index]

    if value == current_elem:
        return current_index
    elif value > current_elem:
        return current_index + binary_search(input_array[current_index+1:], value)
    return binary_search(input_array[:current_index], value)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)