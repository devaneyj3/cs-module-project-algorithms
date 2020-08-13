'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    new_arr = []
    # while loop to loop through array
    for i in range(0, len(arr)):
        # need a nother for to keep track of the other pointer
        # print(arr[i])
        for j in range(0, len(arr)):       
            print(f'{arr[i]}, {arr[j]}')
            # # take value at current index and times it by every index but that one
            if arr[i] != arr[j]:
                print('in if')
                arr[i] *= arr[j]
                new_arr.append(arr[i])
            # else:
            #     return
            # if arr[i + 1] < len(arr):
            #     product *= arr[i + 1]
            #     return product
            # print(product)
            j += 1
        print(new_arr)
        # if arr i is the same as arr j, continue
        # the index you are on times the values of every other index except the current index
        
        
        # arr[0] = 1: 7*3*4 goes back into arr[0] for 84


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [1, 7, 3, 4]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
