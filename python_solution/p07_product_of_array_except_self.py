from time_it import time_it


@time_it
def product_of_array_except_self_brute_force(nums: list[int]) -> list[int]:
    length = len(nums)
    result = [1]*len(nums)

    for k in range(length):
        i, j = 0, length-1
        product = 1

        while i < k:
            product *= nums[i]
            i += 1
        while k < j:
            product *= nums[j]
            j -= 1
        result[i] = product

    return result


@time_it
def product_of_array_except_self_using_division(nums: list[int]) -> list[int]:
    product = 1
    zeroes = 0
    for num in nums:
        if num == 0:
            zeroes += 1
            if zeroes > 1:
                return [0] * len(nums)
            continue

        product *= num

    for i in range(len(nums)):
        if zeroes == 1:
            if nums[i] == 0:
                nums[i] = product
            else:
                nums[i] = 0
        else:
            nums[i] = int(product/nums[i])

    return nums


@time_it
def product_of_array_except_self_using_extra_variable(nums: list[int]) -> list[int]:
    left = nums[:]
    right = nums[:]
    length = len(nums)

    if len(nums) < 2:
        return nums

    for i in range(1, length, 1):
        left[i] = left[i] * left[i-1]

    for i in range(length-2, -1, -1):
        right[i] = right[i] * right[i+1]

    for i in range(length):
        if i==0:
            nums[i] = right[i+1]
        elif i == length-1:
            nums[i] = left[i-1]
        else:
            nums[i] = left[i-1] * right[i+1]
            
    return nums


@time_it
def product_of_array_except_self_optimal(nums: list[int]) -> list[int]:
    length = len(nums)
    if length < 2:
        return nums
    
    result = nums[:]

    for i in range(1, length, 1):
        result[i] *= result[i-1]
    
    product = 1
    for i in range(length-1, 0, -1):
        result[i] = result[i-1] * product
        product *= nums[i]
    result[0] = product

    return result


if __name__ == '__main__':
    items = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [4,3,2,1,2], # [12,16,24,48,24]
        [0, 0]
    ]

    for item in items:
        print(f'Result for {item}: {product_of_array_except_self_brute_force(item)}\n')
        print(f'Result for {item}: {product_of_array_except_self_using_division(item)}\n')
        print(f'Result for {item}: {product_of_array_except_self_using_extra_variable(item)}\n')
        print(f'Result for {item}: {product_of_array_except_self_optimal(item)}\n')

'''
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
'''
