#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next!=None and current.next.next!=None: # 奇数偶数情况都考虑到了。注意不可以写成current.next.next!=None and current.next!=None。因为代码会先判断current.next.next是否为空，此时若current.next为空会报错空指针异常。
            temp = current.next
            temp1 = current.next.next.next
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1 # current.next.next.next = temp1
            current = current.next.next # current = temp
        return dummy_head.next
# @lc code=end

