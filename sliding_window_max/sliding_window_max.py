'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    new_array = []
    start = 0
    # for loops with k number of steps
    for i in range(start, len(nums)):
        # print(f'Start is: {start} k is: {k}')
        window = nums[start:k]
        # print(f'sliding window arr is: {window}')
        # set starting position to increment by one
        start += 1
        k += 1
        max_value = max(window)
        # push max value into new array
        new_array.append(max_value)
        if (k > len(nums)):
            break  
        window = nums[start +1:k + 1]
    return new_array
        # increment sliding window
        # sliding_window_max(nums, k + k)

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
