from time_it import time_it


@time_it
def reverse_vowels_of_a_string(string: str) -> str:
    i = 0
    j = len(string)-1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = list(string)

    while i < j:
        if new_string[i] not in vowels:
            i += 1
        if new_string[j] not in vowels:
            j -= 1
        if new_string[i] in vowels and new_string[j] in vowels:
            new_string[i], new_string[j] = new_string[j], new_string[i]
            i += 1
            j -= 1

    return ''.join(new_string)


if __name__ == "__main__":
    inputs = [
        'IceCreAm',
        'leetcode',
    ]

    for item in inputs:
        print(f"Result for {item}:  {reverse_vowels_of_a_string(item)}\n")


'''
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
'''
