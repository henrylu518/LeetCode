class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def binarySearch(self, sortedNums, target):
        low, high = 0, len(sortedNums) - 1
        while high >= low:
            middle = (high + low) / 2
            if sortedNums[middle] == target:
                return middle
            elif sortedNums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return -1
    
    def search(self, nums, target):
        i, numsLen = 0, len(nums)
        while i < numsLen - 1 and nums[i + 1] > nums[i]:
            i += 1
        sortedNums = nums[i + 1:] + nums[:i + 1]
        index = self.binarySearch(sortedNums, target)
        if index == -1: return -1
        shiftedPosition = numsLen - 1 - i
        index -= shiftedPosition
        if index < 0:   index += numsLen
        return index