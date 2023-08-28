# @before-stub-for-debug-begin
from python3problem142 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast = slow = head
#         while fast != None and fast.next != None: # while中条件为链表有环的必要条件；fast走两步，fast.next不能为空
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 index1 = slow
#                 index2 = head
#                 while index1:
#                     index1 = index1.next
#                     index2 = index2.next
#                     if index1 == index2:
#                         return index1
#         return None
    
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast != None and fast.next != None: # while中条件为链表有环的必要条件；fast走两步，fast.next不能为空
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                index1 = slow
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None

# @lc code=end

