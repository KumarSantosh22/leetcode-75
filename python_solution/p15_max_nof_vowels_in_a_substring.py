from time_it import time_it


@time_it
def max_nof_vowels_in_a_substring(s: str, k: int) -> int:
    pass


if __name__ == '__main__':
    items = [
        ["abciiidef", 3, 3],
        [ "aeiou", 2, 2],
        [ "leetcode", 3, 2]
    ]

    for item in items:
        # result = max_number_of_k_sum_pairs(item[0], item[1])
        result = max_nof_vowels_in_a_substring(item[0], item[1])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[2] else "\033[31mFailed\033[0m"}\n')


'''
1456. Maximum Number of Vowels in a Substring of Given Length
    Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
    1 <= s.length <= 10**5
    s consists of lowercase English letters.
    1 <= k <= s.length
'''