class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n < 0: return False
        visited = set()
        while True:
            sumOfSqure = 0
            if n in visited: return False
            visited.add(n)
            while n:
                sumOfSqure += (n % 10) ** 2
                n /= 10
            if sumOfSqure == 1: return True
            n = sumOfSqure