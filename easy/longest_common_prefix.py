# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(1, len(strs)):
            cur_len = min(len(lcp), len(strs[i]))
            lcp = lcp[:cur_len]
            for j in range(0, cur_len):
                if lcp[j] != strs[i][j]:
                    lcp = lcp[:j]
                    break
        return lcp
