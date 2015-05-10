class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        def combineRecur(nums, remain):
            if remain == 0: return [[]]
            result = []
            for i in xrange(len(nums) - remain + 1):
                result += [[nums[i]] + e for e in combineRecur(nums[i + 1:], remain - 1)]
            return result        
        
        return combineRecur(list(range(1, n + 1)), k)

