"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
注意：

A 和 B 长度不超过 100。

"""


class Solution:
    # 最直接的方法
    def rotateString(self, A: str, B: str) -> bool:
        for _ in range(len(A) + 1):
            if A == B:
                return True
            else:
                A = A[1:] + A[:1]
        return False

    # 将题目转换为 B 是否为 A + A 的字串
    def rotateString1(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in (A + A)


if __name__ == '__main__':
    s = Solution()
    A = 'abcde'
    B = 'abced'
    r = s.rotateString(A, B)
    print(r)
