from time_it import time_it


def greatest_common_divisor_of_strings(str1: str, str2: str) -> str:
    if len(str2) > len(str1):
        return greatest_common_divisor_of_strings(str2, str1)
    if str1 == str2:
        return str1
    if str1.startswith(str2):
        return greatest_common_divisor_of_strings(str1[len(str2):], str2)
    return ""


if __name__ == "__main__":
    words = [
        ["ABCABC", "ABC"],
        ["ABABAB", "ABAB"],
        ["LEET", "CODE"],
        ["abcd", "pq"],
        ["", ""],
    ]
    for word in words:
        print(
            f"GCD of {word[0]} and {word[1]}:  {greatest_common_divisor_of_strings(word[0], word[1])}\n"
        )

"""
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 
Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
