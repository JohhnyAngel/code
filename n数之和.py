# def nSumTarget(nums, n, start, target):
#     sz = len(nums)
#     res = []
    
#     # 至少是 2Sum，且数组大小不应小于 n
#     if n < 2 or sz < n:
#         return res
    
#     # 2Sum 是 base case
#     if n == 2:
#         lo, hi = start, sz - 1
#         while lo < hi:
#             _sum = nums[lo] + nums[hi]
#             left, right = nums[lo], nums[hi]
#             if _sum < target:
#                 while lo < hi and nums[lo] == left:
#                     lo += 1
#             elif _sum > target:
#                 while lo < hi and nums[hi] == right:
#                     hi -= 1
#             else:
#                 res.append([left, right])
#                 while lo < hi and nums[lo] == left:
#                     lo += 1
#                 while lo < hi and nums[hi] == right:
#                     hi -= 1
#     else:
#         # n > 2 时，递归计算 (n-1)Sum 的结果
#         i = start
#         while i < sz:
#             sub = nSumTarget(nums, n - 1, i + 1, target - nums[i])
#             for arr in sub:
#                 # (n-1)Sum 加上 nums[i] 就是 nSum
#                 arr.append(nums[i])
#                 res.append(arr)
#             while i < sz - 1 and nums[i] == nums[i + 1]:
#                 i += 1
#             i += 1
            
#     return res

# nums = [0,0,0]
# n = 3
# start = 0
# target = 0
# nums.sort()
# result = nSum(n, nums, start, target)
# print(result)

def nSum(n, nums, target):
    res = []
    if n == 2:
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i]+nums[j] < target:
                    i += 1
            elif nums[i]+nums[j] > target:
                    j -= 1
            else:
                res.append([nums[i], nums[j]])
                while nums[i+1] == nums[i] and i < j:
                    i += 1
                while nums[j-1] == nums[j] and i < j:
                    j -= 1
                i += 1
                j -= 1
        return res
    
    else:
        i = 0
        while i < len(nums):
            sub = nSum(n-1, nums[i+1:], target-nums[i])
            for arr in sub:
                arr.append(nums[i])
                res.append(arr)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
        
nums = [-1,0,1,2,-1,-4]
n = 3
start = 0
target = 0
nums.sort()
result = nSum(n, nums, target)
print(result)

