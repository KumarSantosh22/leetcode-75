from time_it import time_it


@time_it
def move_zeroes(nums: list[int]) -> None:
    zeroth = 0
    ith = 0
    while ith < len(nums):
        if nums[ith]:
            nums[ith], nums[zeroth] = nums[zeroth], nums[ith]
            zeroth += 1
        ith += 1


if __name__ == '__main__':
    items = [
        [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
        [[0], [0]],
        [[0, 0, 1], [1, 0, 0]]
    ]

    for item in items:
        move_zeroes(item[0])
        print(
            f'\033[33mResult =\033[0m {item[0]}\n==={"\033[32mPassed\033[0m" if item[0] == item[1] else "\033[31mFailed\033[0m"}\n')

'''
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 10**4
-2**31 <= nums[i] <= 2**31 - 1
'''
