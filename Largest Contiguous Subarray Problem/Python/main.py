class Solution:

    def findMaxLength(nums):
        maxlen = 0
        for start in range(0, len(nums)):
            zeroes = 0
            ones = 0
            for end in range(start, len(nums)):
                if nums[end] == 0:
                    zeroes += 1
                else:
                    ones += 1
    
                if zeroes == ones:
                    maxlen = max(maxlen, end - start + 1)
    
        return maxlen