class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        result = x
        high, low = x, 0
        while not (result ** 2 <= x and (result + 1) ** 2 > x):
            if result ** 2 > x:
                high = result 
                result = (result + low) / 2       
            else:
                low = result
                result = (result + high) / 2       
        return result

print Solution().mySqrt(6)