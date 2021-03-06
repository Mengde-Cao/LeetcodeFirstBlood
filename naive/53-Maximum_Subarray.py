"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        https://www.geekxh.com/1.2.%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/202.html#_03%E3%80%81go%E8%AF%AD%E8%A8%80%E7%A4%BA%E4%BE%8B
        """
        dp = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] >= 0:
                dp.append(dp[i - 1] + nums[i])
            else:
                dp.append(nums[i])
        return max(dp)

    def maxSubArray1(self, nums: List[int]) -> int:
        """
        这种更省内存，但是nums发生了变化
        """
        for i in range(1, len(nums)):
            if nums[i - 1] >= 0:
                nums[i] = nums[i - 1] + nums[i]
        return max(nums)
