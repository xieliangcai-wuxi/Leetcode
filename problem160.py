# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 初始化两个指针
        ptrA, ptrB = headA, headB

        # 遍历直到两指针相遇或同时为 None（无交点）
        while ptrA != ptrB:
            # 如果 ptrA 走到末尾，跳转到 headB 继续；否则继续前进
            ptrA = ptrA.next if ptrA else headB
            # 如果 ptrB 走到末尾，跳转到 headA 继续；否则继续前进
            ptrB = ptrB.next if ptrB else headA

        # 返回交点（若不相交，ptrA 和 ptrB 会同时为 None）
        return ptrA

