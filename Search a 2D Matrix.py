class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix == [[]]: return False
        height, width = len(matrix), len(matrix[0])
        low, high = 0, height - 1
        while high >= low:
            middle = (high + low) / 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] > target:
                high = middle - 1
            else:
                low = middle + 1
        row = None
        print low, high
        if high < 0: row = 0
        elif low > height - 1:  row = height - 1
        elif target > matrix[high][-1]: 
            row = low
        else:
            row = high
        low, high = 0, width - 1
        while high >= low:
            middle = (high + low) / 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return False