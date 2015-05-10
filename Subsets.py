class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets_1(self, nums):

        def subsetsOrder(nums):
            if len(nums) == 0: return [[]]
            s = subsetsOrder(nums[1:])
            return s + [[nums[0]] + e for e in s]
            
        return subsetsOrder(sorted(nums))

    def subsets_2(self, nums):
    	
        def subsetsOrder(current, nums):
            if nums:
                return subsetsOrder(current, nums[1:]) + subsetsOrder(current + [nums[0]], nums[1:])
            return [current]
            
        return subsetsOrder([], sorted(nums))
        