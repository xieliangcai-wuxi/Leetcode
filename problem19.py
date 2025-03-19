# Definition for singly-linked list.
from inspect import stack
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # 创建虚拟头节点
        dummy.next = head
        node_stack = []
        current = dummy  # 从虚拟头节点开始遍历

        # 将节点（含虚拟头）全部入栈
        while current:
            node_stack.append(current)
            current = current.next

        # 弹出n次，定位到倒数第n+1个节点
        for _ in range(n):
            node_stack.pop()

        # 此时栈顶是倒数第n+1个节点
        pre = node_stack[-1]
        pre.next = pre.next.next  # 删除倒数第n个节点

        return dummy.next  # 返回虚拟头的next，自动处理头节点删除
