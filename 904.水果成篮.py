#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, result, count = 0, 0, 0
        a = {i:0 for i in range(len(fruits))}
        for j in range(len(fruits)):
            if a[fruits[j]] == 0:
                count += 1
            a[fruits[j]] += 1
            while count > 2:
                a[fruits[i]] -= 1
                if a[fruits[i]] == 0:
                    count -= 1
                i += 1
            result = max(result, j-i+1)
        return result

# @lc code=end

