class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        if n == 1:
            return 1

        res = 1

        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                if i % 2 == 1:
                    res += 1

                j = (n // i)

                if i != j and j % 2 == 1:
                    res += 1
        
        if n % 2 == 1:
            res +=1

        return res