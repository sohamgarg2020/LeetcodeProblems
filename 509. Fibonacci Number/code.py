class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        num1 = 0
        num2 = 1

        for i in range(n-1):
            num1, num2 = num2, num1+num2
        
        return num2

