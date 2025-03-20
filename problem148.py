# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            return None
        list = []
        map = {}
        result = ListNode()
        curr = head
        while curr:
            map[curr.val] = curr
            list.append(curr.val)
            curr = curr.next
        list.sort()
        curr = result
        for i in range(len(list)):
            curr.next = map[list[i]]
            curr = curr.next
        return result.next

    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # 正确判断空链表
            return None

        nodes = []  # 直接存储节点
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # 断开所有节点的旧链接，防止循环
        for node in nodes:
            node.next = None

        # 按节点值排序
        nodes.sort(key=lambda x: x.val)

        # 构建新链表
        dummy = ListNode()
        curr = dummy
        for node in nodes:
            curr.next = node
            curr = curr.next

        return dummy.next  # 返回排序后的头节点
