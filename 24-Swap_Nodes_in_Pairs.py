"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://www.youtube.com/watch?v=xG3Z0jroOxc
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def recur(node: ListNode):
            if not node or not node.next:
                return node
            tmp = node.next
            node.next = recur(node.next.next)
            tmp.next = node
            return tmp

        return recur(head)


if __name__ == '__main__':
    pass
