"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
通过次数135,100提交次数257,315

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

"""
哈希计数法
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        r = list()
        for n in nums1:
            d1[n] += 1
        for m in nums2:
            d2[m] += 1
        for k in d1:
            if d2[k]:
                r.extend([k] * min(d1[k], d2[k]))
        return r


"""
排序双指针
"""


class Solution1:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        # 对输入的数组排序
        nums1.sort()
        nums2.sort()
        # 结果集
        r = list()
        # 左右指针
        left, right = 0, 0
        # 移动指针
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                r.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1
        return r
