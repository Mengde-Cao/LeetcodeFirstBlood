"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
通过次数525,846提交次数1,380,349

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        result = cur
        flag = 0
        while l1 or l2:
            val = flag
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            flag = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
        if flag:
            cur.next = ListNode(1)
        return result.next


if __name__ == '__main__':
    h1 = ListNode(3)
    h1.next = ListNode(1)
    h2 = ListNode(7)
    h2.next = ListNode(3)
    h2.next.next = ListNode(1)
    s = Solution()
    r = s.addTwoNumbers(ListNode(5), ListNode(5))
    while r:
        print(r.val)
        r = r.next
