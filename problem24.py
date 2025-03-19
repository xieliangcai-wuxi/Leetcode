from typing import Optional

from boltons.iterutils import first


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 虚拟头节点，统一处理头节点交换
        dummy.next = head
        pre = dummy  # 前驱节点，用于连接交换后的组
        curr = head  # 当前遍历指针

        while curr and curr.next:
            # 将两个节点压入栈
            stack = []
            for _ in range(2):
                stack.append(curr)
                curr = curr.next

            # 弹出栈中的节点（逆序）
            second = stack.pop()  # 第二个节点
            first = stack.pop()  # 第一个节点

            # 连接前驱节点到新头（second）
            pre.next = second
            # 连接当前组的下一个节点（原下一组的起始节点）
            first.next = curr
            # 连接两个交换后的节点
            second.next = first

            # 更新前驱节点到当前组的末尾（first）
            pre = first

        return dummy.next

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 虚拟头节点，处理头节点交换
        dummy.next = head
        pre = dummy  # 前驱节点，用于连接交换后的组

        while pre.next and pre.next.next:
            node1 = pre.next  # 当前第一个节点
            node2 = node1.next  # 当前第二个节点
            next_group = node2.next  # 下一组的起始节点

            # 交换 node1 和 node2
            pre.next = node2  # 前驱指向新头
            node2.next = node1  # node2 -> node1
            node1.next = next_group  # node1 连接下一组

            pre = node1  # 前驱移动到当前组的末尾（即node1）

        return dummy.next  # 返回虚拟头的next，自动处理新头节点