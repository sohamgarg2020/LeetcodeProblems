from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            freq_s = defaultdict(int)
            freq_t = defaultdict(int)
            for i in s:
                freq_s[i] += 1
            for i in t:
                freq_t[i] += 1
            return freq_s==freq_t
        return False
