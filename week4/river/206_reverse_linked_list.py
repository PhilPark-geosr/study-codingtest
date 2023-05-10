# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_ = current.next_
            current.next_ = prev
            prev = current
            current = next_
        return prev


head = ListNode(1)
head.next_ = ListNode(2)
head.next_.next_ = ListNode(3)
head.next_.next_.next_ = ListNode(4)
head.next_.next_.next_.next_ = ListNode(5)
print(head)

reversed_list = Solution.reverse_list(head)
node = reversed_list
s = list()
while node:
    s.append(node.val)
    node = node.next_
print(s)
