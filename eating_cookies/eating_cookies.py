'''
Input: an integer
Returns: an integer
'''

from itertools import permutations
def eating_cookies(n):
    # if we eat less than 1 cookie
    if n <= 1:
        return 1
    
    # go through all permutations of possible combinations
    # for eating cookies
    for i in permutations(range(n)):
        print(i) 
    # how can ways can we eat 5 cookies 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
