"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
通过次数308,352提交次数1,057,233
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先对数组排序
        nums.sort()
        n = len(nums)
        # 结果集
        result = []
        # 固定一个数，然后在其右侧通过双指针寻找目标值
        for i in range(n):
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # 左指针右移，右指针左移，跳到重复值中的最后一个
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                # 和大于0，右指针左移
                elif sum > 0:
                    r -= 1
                # 和小于0，左指针右移
                else:
                    l += 1
        return result
