'''
Input: a List of integers
Returns: a List of integers
'''
import math

# TODO: I NEED HELP WITH THIS

# def product_of_all_other_numbers(arr):
#     new_arr = []
    
#     # loop from start of list
#     for i in range(0, len(arr)):
#         print(f'from start of lis {arr[i]}')
#         i += 1
#     for j in range(len(arr) -1):  
#         print(arr[j])
#         j -= 1
#         # if arr i is the same as arr j, continue
#         # the index you are on times the values of every other index except the current index
#         # arr[0] = 1: 7*3*4 goes back into arr[0] for 84

def product_of_all_other_numbers(arr):
    # prints [0,0,0,0] to have a temp new array
    final_arr = [0] * len(arr)
    # print(final_arr)
    for i, elem in enumerate(arr):
        j = i + 1
        # print(f'counter j is {j} and i is {i}') 
        new_arr = arr[:i] + arr[j:] if i != 0 else arr[j:]
        # print(new_arr)
        elem = math.prod(new_arr)
        # print(elem)
        final_arr[i] = elem
    return final_arr



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [1, 7, 3, 4]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
