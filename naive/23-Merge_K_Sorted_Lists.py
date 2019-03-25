"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
将K个有序链表的合并分解为两两合并
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        if len(lists) < 1:
            return []
        return self.helper(lists, 0, len(lists) - 1)

    # 分治，跟二分排序差不多
    def helper(self, lists, start, end):
        if start >= end:
            return lists[start]
        left = self.helper(lists, start, (start + end) // 2)
        right = self.helper(lists, (start + end) // 2 + 1, end)
        return self.mergeTwoList(left, right)

    def mergeTwoList(self, l1: ListNode, l2: ListNode):
        if not (l1 or l1.val):
            return l2
        if not (l2 or l2.val):
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
