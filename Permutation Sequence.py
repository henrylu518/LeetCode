class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        factor = [1, 1]
        for i in xrange(2, n + 1):
            factor.append(factor[-1] * i)
        nums = list(range(1, n + 1))
        result = ''
        for i in xrange(n, 0, -1):
            index = k / factor[i - 1] 
            if k % factor[i - 1] != 0: index += 1
            result += str(nums[index - 1])
            nums.pop(index - 1)
            k = k % factor[i - 1]
        return result