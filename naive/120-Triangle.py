"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]
        dp = []
        for t in triangle:
            dp.append([0] * len(t))
        dp[0][0] = triangle[0][0]
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[1][1] = triangle[0][0] + triangle[1][1]
        for i in range(2, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][0]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
        return min(dp[-1])


if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    r = s.minimumTotal(tri)
    print(r)
