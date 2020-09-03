'''
Input: an integer
Returns: an integer
'''

# use memoization for large input to remember computations that are repeated

def eating_cookies(n):
    # if we eat less than 1 cookie
    if n < 0:
        return 0
    elif n == 0:
        return 1
#     5 cookies = 13 diffent ways to eat the cookies
    else:
        # TODO: I NEED AN EXPLANATION OF THIS     13 -2                  13-1
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
    #                     10                    11                  12
    #                      7                    9                   11
    #                      4                    7                   10
    #                       1                   5                   9
    #                       -2                  3                   8
    #                returns 0                  1                   7
    #                                                               6
    #                                                               5
    #                                                               4
    #                                                               3
    #                                                               2
    #                                                               1
    #                                                               0
    #                                                               0 returns 1

    return n

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 13 
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
