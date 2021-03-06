"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    cur = ListNode(None)
    cur.next = head
    result = cur
    i = 0
    while head:
        # cur 移动 L - n 次
        if i >= n:
            cur = cur.next
        head = head.next
        i += 1
    # 此时 cur 位于倒数第 n - 1 个节点
    cur.next = cur.next.next
    return result.next
