from time_it import time_it


@time_it
def max_consecutive_ones(nums: list[int], k: int) -> int:
    pass


if __name__ == '__main__':
    items = [
        [[1,1,1,0,0,0,1,1,1,1,0], 2, 6],
        [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10]
    ]

    for item in items:
        # result = max_number_of_k_sum_pairs(item[0], item[1])
        result = max_consecutive_ones(item[0], item[1])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[2] else "\033[31mFailed\033[0m"}\n')


'''
1004. Max Consecutive Ones III
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
    1 <= nums.length <= 10**5
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
'''