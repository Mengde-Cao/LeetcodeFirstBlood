"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""


def majorityElement(nums: list[int]) -> int:
    # 遍历数组, 依次消除不同的数字, 剩下的为众数
    key, count = None, 0
    for i in nums:
        if not key:
            key, count = i, 1
        else:
            if key == i:
                count += 1
            else:
                count -= 1
        if count == 0:
            key = None
    return key


def majorityElement(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]
