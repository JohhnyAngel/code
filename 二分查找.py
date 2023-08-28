class Solution:
    def search(self, nums, target) -> int:
        left = 0 
        right = len(nums)
        while left < right:
            middle = left + ((right-left)//2)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return middle
        return -1

solution = Solution()
nums = [-1,0,3,5,9,12]
solution.search(nums, 9)