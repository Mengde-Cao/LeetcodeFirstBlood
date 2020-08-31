"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。
"""

"""
ord: 字节对应的unicode码点, ord('a') = 97
chr: unicode码点对应的字节, chr(97) = 'a'
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s:
            # 第一次遍历，记录每个字母最后一次出现的位置对应的索引
            letter_last_indexes = [-1] * 26
            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                if letter_last_indexes[index] == -1:
                    letter_last_indexes[index] = i
                else:
                    letter_last_indexes[index] = -2
            # 第二次遍历，如果字符第一次出现位置为最后一次出现的位置，则直接返回
            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                if letter_last_indexes[index] >= 0 and letter_last_indexes[index] == i:
                    return i
        return -1

    def firstUniqChar1(self, s: str) -> int:
        if s:
            appearance = dict()
            for i in range(len(s)):
                if s[i] not in appearance:
                    appearance[s[i]] = i
                else:
                    appearance[s[i]] = -1
            # 第二次遍历，如果字符第一次出现位置为最后一次出现的位置，则直接返回
            for i in range(len(s)):
                if appearance[s[i]] == i and appearance[s[i]] >= 0:
                    return i
        return -1

    def firstUniqChar2(self, s: str) -> int:
        for letter in s:
            l_index = s.find(letter)
            r_index = s.rfind(letter)
            if l_index == r_index and l_index >= 0:
                return l_index
        return -1


if __name__ == '__main__':
    s = Solution()
    i1 = "leetcode"
    i2 = "loveleetcode"
    i3 = "cc"
    r1 = s.firstUniqChar2(i1)
    r2 = s.firstUniqChar2(i2)
    r3 = s.firstUniqChar2(i3)
    print(r1, r2, r3)
