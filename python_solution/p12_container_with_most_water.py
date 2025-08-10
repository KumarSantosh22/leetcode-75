from time_it import time_it


@time_it
def container_with_most_water_brute_force(height: list[int]) -> int:
    max_amt = 0
    length = len(height)
    for i in range(length):
        for j in range(length):
            amt = (j-i) * min(height[i], height[j])
            if amt > max_amt:
                max_amt = amt
    return max_amt


@time_it
def container_with_most_water(height: list[int]) -> int:
    max_amt = 0
    l, r = 0, len(height)-1
    
    while l < r:
        amt = (r-l) * min(height[l], height[r])
        if amt > max_amt:
            max_amt = amt

        if height[l] < height[r]:
            l =+ 1
        else:
            r -= 1
    return max_amt


if __name__ == '__main__':
    items = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
        [[1, 1], 1]
    ]

    for item in items:
        # result = container_with_most_water_brute_force(item[0])
        result = container_with_most_water(item[0])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[1] else "\033[31mFailed\033[0m"}\n')

'''
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4
'''
