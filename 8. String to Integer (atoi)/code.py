class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        i = 0
        INT_MAX = 2**31-1
        INT_MIN = -(2**31)
        neg = 1
        if s[0] == "-":
            neg = -1
            i+= 1
        elif s[0] == "+":
            i+=1
        res = 0
        
        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])

            if res* neg > INT_MAX:
                return INT_MAX
            elif res*neg < INT_MIN:
                return INT_MIN
            
            i+= 1
        return res*neg

