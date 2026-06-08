from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # This solution will work if array is sorted
    i = 0
    j = len(nums) - 1
    while i < j:
        result = nums[i] + nums[j]
        if result == target:
            return [i, j]
        elif result > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]


def two_sum_for_all(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i