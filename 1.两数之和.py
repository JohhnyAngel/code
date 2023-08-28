#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            if target - nums[i] in record:
                return [i, record[target - nums[i]]]
            record[nums[i]] = i
        # return []
            
# @lc code=end

