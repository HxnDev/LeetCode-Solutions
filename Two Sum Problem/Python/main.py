class Solution(object):
    def twoSum(self, nums, target):

        result = []
        index_map = {}

        for i, n in enumerate(nums):
            difference = target - nums

            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = if

        return sorted(result)