
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):

        def searchLeft():
            low, high = 0, len(nums) - 1
            while high >= low:
                middle = (high + low) / 2
                if nums[middle] == target:
                    if middle > low:
                        if nums[middle - 1] != target:
                            return middle
                        else:
                            high = middle - 1
                    else:
                        return middle
                elif nums[middle] > target:
                    high = middle - 1
                else:
                    low = middle + 1
            return -1
        
        def searchRight():
            low, high = 0, len(nums) - 1
            while high >= low:
                middle = (high + low) / 2
                if nums[middle] == target:
                    if middle < high:
                        if nums[middle + 1] != target:
                            return middle
                        else:
                            low = middle + 1
                    else:
                        return middle
                elif nums[middle] > target:
                    high = middle - 1
                else:
                    low = middle + 1
            return -1

        left = searchLeft()
        if left == -1: return [-1, -1]
        right = searchRight()
        return [left, right]
        