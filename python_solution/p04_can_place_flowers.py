from time_it import time_it


@time_it
def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True

    for i in range(len(flowerbed)):
        left = (i == 0) or (flowerbed[i-1] == 0)
        right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
        if left and right and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
        if n == 0:
            return True

    return False


if __name__ == "__main__":
    inputs = [
        [[1, 0, 0, 0, 1], 1],
        [[1, 0, 0, 0, 1], 2],
    ]

    for item in inputs:
        print(
            f"Result for {item[0]} and {item[1]}:  {can_place_flowers(item[0], item[1])}\n"
        )

'''
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''
