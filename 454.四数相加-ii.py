#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        record = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                record[-nums1[i]-nums2[j]] = record.get(-nums1[i]-nums2[j], 0) + 1
        for i in range(n):
            for j in range(n):
                if nums3[i]+nums4[j] in record:
                    result += record[nums3[i]+nums4[j]]
        return result
        
# @lc code=end

