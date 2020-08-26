"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

通过次数214,887提交次数437,567
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        # 快慢指针法，就像两个速度不同的人在操场上跑圈，若跑得快的与跑得慢的相遇（超了一圈），则说明有环。
        # 二者起点不能相同
        fast = head.next
        while head and fast and fast.next:
            if fast == head:
                return True
            # 慢的跑一步
            head = head.next
            # 快的跑两步
            fast = fast.next.next
        return False
