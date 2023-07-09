# https://leetcode.com/contest/biweekly-contest-107/problems/find-maximum-number-of-string-pairs/

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        pairs = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] == words[j][::-1]:
                    pairs += 1

        return pairs
