class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        skip_val = (numRows * 2) - 2

        for i in range(numRows):
            idx = i
            if idx >= len(s): break

            result.append(s[idx])

            skip_iter = skip_val - 2*i if 0 < i < numRows-1 else skip_val

            while True:
                idx += skip_iter
                if idx >= len(s): break

                result.append(s[idx])

                if 0 < i < numRows-1:
                    skip_iter = skip_val - skip_iter
            
        return "".join(result)
