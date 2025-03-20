from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map = {}
        dummy = head
        while dummy:
            map[dummy] = Node(dummy.val)
            dummy = dummy.next
        dummy = head
        while dummy:
            if dummy.next:
                map[dummy].next = map[dummy.next]
            # 设置新节点的 random（指向新节点，而非原节点）
            if dummy.random:
                map[dummy].random = map[dummy.random]
            else:
                map[dummy].random = None  # 处理 random 为 None
            dummy = dummy.next
        return map[head]