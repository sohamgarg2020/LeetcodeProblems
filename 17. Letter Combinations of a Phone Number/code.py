class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def letter(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for i in phone[next_digits[0]]:
                letter(combination + i, next_digits[1:])
        letter("", digits)
        return res
