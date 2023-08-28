# def SetPrefix(Pattern):
#     len_pattern = len(Pattern)  # 模式字符串长度。
#     prefix = [0] * len_pattern

#     prefix[0] = 0

#     for i in range(1, len_pattern):
#         k = prefix[i - 1]

#         '''
#         当前字符Pattern[i](Pattern[:i+1]的最后一个字符)与最长相同字符前缀的下一个字符Pattern[k]不相等时，
#         不能再直接累加prefix[i] = k + 1，
#         需要不断递归判断是否存在子对称，k=0说明不再有子对称，
#         Pattern[i] != Pattern[k]说明虽然对称，但是对称后面的值和当前的字符值不相等，
#         所以继续递推
#         '''
#         while Pattern[i] != Pattern[k] and k != 0: # k等于0不止代表Pattern[k]到了字符串第一个字符，还有prefix[k]为0也就是说内部不存在后面紧接着Pattern[i]的子对称
#             k = prefix[k - 1]  # 继续递归

#         if Pattern[i] == Pattern[k]:  # 找到了这个子对称，或者是直接继承了前面的对称性，这两种都在前面的基础上++
#             prefix[i] = k + 1
#         else:
#             prefix[i] = 0  # 如果遍历了所有子对称都无效，说明这个新字符不具有对称性，清0
#     return prefix

# pattern = "agctagcagctagct"
# result_prefix = SetPrefix(pattern)
# print(result_prefix)

def getNext(next, s) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
            
            
# 示例模式字符串
pattern = "agctagcagctagct"
next = [0] * len(pattern)
getNext(next, pattern)
print(next)
print(1)
