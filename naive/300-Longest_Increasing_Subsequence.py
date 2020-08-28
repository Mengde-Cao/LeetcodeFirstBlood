"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
from typing import List


class Solution:
    # O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [1] * n
        result = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result

    # O(n*log(n))
    def lengthOfLIS1(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size
        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue

            l, r = 0, len(cell) - 1
            while l < r:
                mid = l + (r - l) // 2
                if cell[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num
        return len(cell)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS1(nums))
