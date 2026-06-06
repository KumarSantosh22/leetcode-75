from time_it import time_it


@time_it
def merge_strings_alternately(word1: str, word2: str) -> str:
    i: int = 0
    word: str = ""
    if len(word1) > len(word2):
        while i < len(word2):
            word += word1[i] + word2[i]
            i += 1
        while i < len(word1):
            word += word1[i]
            i += 1
    else:
        while i < len(word1):
            word += word1[i] + word2[i]
            i += 1
        while i < len(word2):
            word += word2[i]
            i += 1
    return word


@time_it
def merge_alternately(word1: str, word2: str) -> str:
    i: int = 0
    word: str = ""

    if len(word1) > len(word2):
        while i < len(word2):
            word += word1[i] + word2[i]
            i += 1
        word += word1[i:]
    else:
        while i < len(word1):
            word += word1[i] + word2[i]
            i += 1
        word += word2[i:]

    return word


@time_it
def optimized_merge(word1: str, word2: str) -> str:
    result = ""
    len1 = len(word1)
    len2 = len(word2)

    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            result += word1[i]
        if i < len2:
            result += word2[i]
    result


if __name__ == "__main__":
    words = [
        ["cat", "mat"],
        ["abc", "pqr"],
        ["ab", "pqrs"],
        ["abcd", "pq"],
        ["", "a"],
        ["a", ""],
        ["", ""],
    ]
    for word in words:
        print(f"New string: {merge_strings_alternately(word[0], word[1])}\n")
        print(f"New string: {merge_alternately(word[0], word[1])}\n")
        print(f"New string: {optimized_merge(word[0], word[1])}\n")


"""
1768. Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
