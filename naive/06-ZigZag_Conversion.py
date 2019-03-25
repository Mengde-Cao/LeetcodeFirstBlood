'''
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
'''


def convert(self, s: 'str', numRows: 'int') -> 'str':
    if len(s) <= numRows or numRows < 2:
        return s
    r = []
    i = 0
    while i < len(s):
        if i == 0 or i % (2 * numRows - 2) == 0:  # 从上往下
            t = ['-'] * numRows
            for p in range(numRows):
                t[p] = s[i]
                i += 1
                if i >= len(s):
                    break
            r.append(t)
            # print(t)
        else:  # 从下往上
            m = ['-'] * numRows
            for p in range(1, numRows - 1):
                m[numRows - p - 1] = s[i]
                i += 1
                if i >= len(s):
                    break
            r.append(m)
            # print(m)
    result = ''
    # rr 为二阶矩阵，转置后为Z形
    for ii in range(numRows):
        for rr in r:
            result += rr[ii]
    return result.replace('-', '')


if __name__ == '__main__':
    r = convert("ABCDEF", 4)
    print(r)
