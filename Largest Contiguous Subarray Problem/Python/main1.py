class Solution:

    def findMaxLength(self, nums):
        count = 0
        map = {0:-1}
        maxlen = 0

        for i, number in enumerate(nums):
            if number:
                count += 1
            else:
                count -= 1

            if count in map:
                maxlen = max(maxlen, (i-map[count]))
            else:
                map[count] = 1

        return maxlen