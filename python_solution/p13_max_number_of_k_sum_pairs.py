from time_it import time_it


@time_it
def max_number_of_k_sum_pairs(nums: list[int], k: int) -> int:
    # solution using two pointers
    # step1: sort the array
    nums.sort()
    # step2: apply alogorithm
    print(nums)
    i, j = 0, len(nums)-1
    count = 0

    while i < j:
        t = nums[i] + nums[j]
        if t == k:
            count += 1
            i += 1
            j -= 1
        elif t < k:
            i += 1
        else:
            j -= 1
    return count


@time_it
def max_number_of_k_sum_pairs_using_map(nums: list[int], k: int) -> int:
    # solution using map
    frequency = {}
    count = 0

    for num in nums:
        target = k - num
        if target in frequency and frequency[target] > 0:
            count += 1
            frequency[target] -= 1
        else:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    return count


if __name__ == '__main__':
    items = [
        [[1, 2, 3, 4], 5, 2],
        [[3, 1, 3, 4, 3], 6, 1],
    ]

    for item in items:
        # result = max_number_of_k_sum_pairs(item[0], item[1])
        result = max_number_of_k_sum_pairs_using_map(item[0], item[1])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[2] else "\033[31mFailed\033[0m"}\n')

'''
1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

1 <= nums.length <= 10**5
1 <= nums[i] <= 10**9
1 <= k <= 10**9
'''
