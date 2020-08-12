'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    return [noneZero for noneZero in arr if noneZero != 0] + [Zero for Zero in arr if Zero == 0]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")