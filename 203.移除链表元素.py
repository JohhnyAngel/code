# @before-stub-for-debug-begin
from python3problem203 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        current = dummy_head
        while current.next:            
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next
# @lc code=end

