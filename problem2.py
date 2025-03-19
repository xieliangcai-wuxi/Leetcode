# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 哑节点作为起始点
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            sum_val = carry  # 初始值包括进位

            # 处理当前位的值
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            if sum_val >= 10:
                carry = 1
            else:
                carry = 0
            val = sum_val%10
            # 计算进位和当前值
            current.next = ListNode(val)  # 创建新节点
            current = current.next  # 移动指针
        return dummy.next  # 返回哑节点的下一个节点，即结果链表的头