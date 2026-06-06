from time_it import time_it


@time_it
def find_max_average(nums: list[int], k: int) -> float:
    pass


if __name__ == '__main__':
    items = [
        [[1, 12, -5, -6, 50, 3], 4, 12.75000],
        [[5], 1, 5.0000]
    ]

    for item in items:
        # result = max_number_of_k_sum_pairs(item[0], item[1])
        result = find_max_average(item[0], item[1])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[2] else "\033[31mFailed\033[0m"}\n')


'''
643. Maximum Average Subarray I
    You are given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10**-5 will be accepted.

Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

Constraints:
    n == nums.length
    1 <= k <= n <= 10**5
    -104 <= nums[i] <= 10**4
'''
