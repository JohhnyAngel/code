class Solution:
    def replaceSpace(self, s: str) -> str:
        count = 0
        for i in s:
            if i == ' ':
                count += 1
        res = list(s)
        res.extend([' ']*count*2)
        i ,j = len(s) - 1, len(res) - 1
        while i:
            if res[i] == ' ':
                res[j-2:j+1] = '%20'
                j -= 3
                i -= 1
                continue
            res[j] = res[i]
            i -= 1
            j -= 1
        return ''.join(res)

sol = Solution()
s = ''
result = sol.replaceSpace(s)
print(result)