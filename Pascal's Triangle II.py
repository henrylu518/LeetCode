class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        current = [1]
        for _ in xrange(rowIndex):
            next = []
            for i in xrange(len(current) + 1):
                if i == 0:
                    next.append(current[0])
                elif i > 0 and i < len(current):
                    next.append(current[i - 1] + current[i])
                else:
                    next.append(current[i - 1])
            current = next
        return current