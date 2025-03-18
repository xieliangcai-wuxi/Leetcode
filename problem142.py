# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        while head:
            if head not in list:
                list.append(head)
                head = head.next
            else:
                return head

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        slow = head
        fast = head
        has_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
            # 寻找环的入口
        p = head
        q = slow
        while p != q:
            p = p.next
            q = q.next

        return p