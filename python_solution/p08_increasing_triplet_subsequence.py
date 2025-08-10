from time_it import time_it


@time_it
def increasing_triplet_subsequence_optimal(nums: list[int]) -> bool:
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
        
    return False


@time_it
def increasing_triplet_subsequence_brute_force(nums: list[int]) -> bool:
    length = len(nums)

    if length < 3:
        return False

    for i in range(length-2):
        j = i+1
        while j < length-1:
            if nums[i] < nums[j]:
                k = i+2
                while k < length:
                    if nums[j] < nums[k]:
                        if i < j < k:
                            print(f'Value: {nums[i]}, {nums[j]}, {nums[k]}')
                            print(f'Index : {i}, {j}, {k}')
                            return True
                    k += 1
            j += 1

    return False


if __name__ == '__main__':
    items = [
        [[1, 2, 3, 4, 5], True],
        [[5, 4, 3, 2, 1], False],
        [[2, 1, 5, 0, 4, 6], True],
        [[20, 100, 10, 12, 5, 13], True],
        [[1, 5, 0, 4, 1, 3], True],
        [[0, 4, 2, 1, 0, -1, -3], False],
        [[0, 0], False]
    ]

    for item in items:
        # result = increasing_triplet_subsequence_brute_force(item[0])
        # print(f'Result for {item[0]}: {result}\n==={"Passed" if result == item[1] else "Failed"}\n')

        result = increasing_triplet_subsequence_optimal(item[0])
        print(
            f'Result for {item[0]}: {result}\n==={"Passed" if result == item[1] else "Failed"}\n')

'''
334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
'''
