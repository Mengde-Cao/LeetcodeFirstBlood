"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if len(s) <= numRows or numRows < 2:
            return s
        r = [""] * numRows
        # i 为对应的行索引，flag 为行索引变化的方向
        # https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
        i, flag = 0, -1
        for ch in s:
            # 走到头了，调头
            if i == 0 or i == numRows - 1:
                flag = -flag
            r[i] += ch
            i += flag
        return "".join(r)
