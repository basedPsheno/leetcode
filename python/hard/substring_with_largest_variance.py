# https://leetcode.com/problems/substring-with-largest-variance/

class Solution:
    def largestVariance(self, s: str) -> int:
        letters = set(s)
        occurrences = {c: [] for c in letters}
        for i, c in enumerate(s):
            occurrences[c].append(i)
        
        # Alias
        occ = occurrences
        
        best = 0
        for a in letters:
            for b in letters:
                if a == b: continue
                ptr_a = 0
                ptr_b = 0
                occ_a = occ[a]
                occ_b = occ[b]
                len_a = len(occ_a)
                len_b = len(occ_b)
                found_a = False
                found_b = False

                best_sum = float('-inf')
                max_curr = 0
                while ptr_a < len_a and ptr_b < len_b:
                    if occ_a[ptr_a] < occ_b[ptr_b]:
                        ptr_a += 1
                        max_curr += 1
                        if found_b: best_sum = max(max_curr, best_sum)
                        else: best_sum = max(max_curr - 1, best_sum)
                    else:
                        found_b = True
                        ptr_b += 1
                        max_curr -= 1
                        if max_curr < 0: 
                            max_curr = 0
                            found_b = False
                
                max_curr += len_a - ptr_a
                best_sum = max(max_curr - (0 if found_b else 1), best_sum)
                print(f"max variance between {a} and {b} is {best_sum}")
                best = max(best_sum, best)
        return best




                
                
