"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        # 双指针
        l = 0
        r = len(s) - 1
        while l < r:
            l_char = s[l]
            r_char = s[r]
            # 字母或数字
            if l_char.lower() == r_char.lower():
                l += 1
                r -= 1
                continue
            # 左指针不为字母或数字
            elif not l_char.isalpha() and not l_char.isdigit():
                l += 1
                continue
            # 右指针不为字母或数字
            elif not r_char.isalpha() and not r_char.isdigit():
                r -= 1
                continue
            # 跳过所有非字母和非数字，如果还不相等，则直接返回False
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    i1 = "A man, a plan, a canal: Panama"
    i2 = "race a car"
    r1 = s.isPalindrome(i1)
    r2 = s.isPalindrome(i2)
    print((r1, r2))
