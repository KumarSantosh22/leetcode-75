from time_it import time_it


@time_it
def is_subsequence(s: str, t: str) -> bool:
    if len(s) < 1:
        return True
    
    i = 0
    length = len(s)
    for ch in t:
        if ch == s[i]:
            i += 1
            if i == length:
                return True
    return False

if __name__ == '__main__':
    items = [
        ["abc", "ahbgdc", True],
        ["axc", "ahbgdc", False],
        ["", "ahbgdc", False]
    ]

    for item in items:
        result = is_subsequence(item[0], item[1])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[2] else "\033[31mFailed\033[0m"}\n')

'''
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input:  s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10**4
s and t consist only of lowercase English letters.
'''
