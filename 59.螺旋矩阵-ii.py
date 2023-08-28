#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int):
        result = [[0]*n for _ in range(n)]
        startx = 0
        starty = 0
        count = 1
        mid = n // 2
        for offset in range(1, mid+1):
            for j in range(starty, n-offset):
                result[startx][j] = count
                count += 1
            for i in range(startx, n-offset):
                result[i][n-offset] = count
                count += 1
            for j in range(n-offset, starty, -1):
                result[n-offset][j] = count
                count += 1
            for i in range(n-offset, startx, -1):
                result[i][starty] = count
                count += 1
            startx += 1
            starty += 1    
        if n % 2 == 1:
            result[mid][mid] = count
        return result

# solution = Solution()
# solution.generateMatrix(4)
# @lc code=end

