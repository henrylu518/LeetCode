class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        y = 0
        while x:
            y = 10*y + x % 10
            x /= 10
        if y > 2 ** 31: return 0
        return sign * y