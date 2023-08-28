#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def nSum(self, nums, n, target):
        res = []
        if n == 2:
            i = 0
            j = len(nums)-1
            while i < j:
                if nums[i]+nums[j] < target and i < j:
                    i += 1
                elif nums[i]+nums[j] > target and i < j:
                    j -= 1
                else:
                    res.append([nums[i],nums[j]])
                    while i < j and nums[i+1]==nums[i]:
                        i += 1
                    while i < j and nums[j-1]==nums[j]:
                        j -= 1
                    i += 1
                    j -= 1
            return res
        else:
            i = 0
            while i < len(nums):
                sub = self.nSum(nums[i+1:], n-1, target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < len(nums)-1 and nums[i+1]==nums[i]:
                    i += 1
                i += 1
            return res
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = self.nSum(nums, 4, target)
        return result
               
# @lc code=end

