from time_it import time_it


@time_it
def func(s: str, k: int) -> int:
    pass


if __name__ == '__main__':
    items = [
        # [['Input'], 'Output'],
        [['a'], 'a'],
        [['b'], 'b'],
        [['c'], 'c']
    ]

    for item in items:
        # result = max_number_of_k_sum_pairs(item[0], item[1])
        result = func(item[0])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[1] else "\033[31mFailed\033[0m"}\n')


'''
Leetcode Problem No. 
    PROBLEM STATEMENT

Example 1:
    Input: nums = [1,1,0,1]
    Output: 3
    Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
    Input: nums = [0,1,1,1,0,1,1,0,1]
    Output: 5
    Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
    Input: nums = [1,1,1]
    Output: 2
    Explanation: You must delete one element.

Constraints:
    1 <= nums.length <= 10**5
    nums[i] is either 0 or 1.
'''
