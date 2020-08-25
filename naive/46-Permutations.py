"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        nums.sort()

        def _permute(r, p, s):
            if not s:
                r.append(p)
            for i in range(len(s)):
                _permute(result, p + [s[i]], s[:i] + s[i + 1:])

        _permute(result, [], nums)
        return result


# Recursion
class Solution1:

    def permute(self, nums):
        # write your code here
        def _permute(result, temp, nums):
            """
            see pic/46_recursion.jepg.
            :param temp: The traversed nodes.
            :param nums: The nodes to be traversed.
            """
            if nums == []:
                result += [temp]
                print('result: %s' % result)
            else:
                for i in range(len(nums)):
                    args = (result, temp + [nums[i]], nums[:i] + nums[i + 1:])
                    print(*(args[1:]))
                    _permute(*args)

        if nums is None:
            return []

        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result


# Non-Recursion
class Solution2:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if nums is None:
            return []
        if nums == []:
            return [[]]
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    s.permute(nums)
