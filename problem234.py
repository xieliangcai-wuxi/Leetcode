# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        for i in range(len(list)):
            if list[i] != list[len(list) - i - 1]:

                return False
        return True