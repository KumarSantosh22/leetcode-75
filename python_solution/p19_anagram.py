from time_it import time_it


@time_it
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    str1 = {}
    str2 = {}

    for i in range(len(s)):
        if s[i] in str1:
            str1[s[i]] += 1
        else:
            str1[s[i]] = 1

        if t[i] in str2:
            str2[t[i]] += 1
        else:
            str2[t[i]] = 1

    for k, v in str1.items():
        print(k)
        if str2.get(k) != v:
            return False
    return True


@time_it
def is_anagram_optimal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1
    for ch in t:
        frequency[ch] = frequency.get(ch, 0) - 1

    return all(count == 0 for count in frequency.values())


if __name__ == '__main__':
    items = [
        # [['Input'], 'Output'],
        [['carrace', 'racecar'], True],
        [['aa', 'bb'], False],
    ]

    for item in items:
        # result = max_number_of_k_sum_pairs(item[0], item[1])
        result = is_anagram_optimal(item[0][0], item[0][1])
        print(
            f'\033[33mResult =\033[0m {result}\n==={"\033[32mPassed\033[0m" if result == item[1] else "\033[31mFailed\033[0m"}\n')
