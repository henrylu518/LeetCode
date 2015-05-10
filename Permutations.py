class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        def permuteLeftWith(result, current, numsLeft):
            if len(numsLeft) == 1: 
                result.append(current + numsLeft)
            else:
                for i in xrange(len(numsLeft)):
                    permuteLeftWith(result, current + [numsLeft[i]], \
                    numsLeft[:i] + numsLeft[i + 1:])
                    
        if nums == []: return []
        result = []
        permuteLeftWith(result, [], nums)
        return result