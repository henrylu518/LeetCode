class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        zero, two = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            elif nums[i] == 2 and i < two:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                i += 1

    def sortColors_2(self, nums):
        lastZero, firstTwo = -1, len(nums)
        i = 0
        while i < firstTwo:
            if nums[i] == 0:
                lastZero += 1
                nums[i], nums[lastZero] = nums[lastZero], nums[i]
            elif nums[i] == 2:
                firstTwo -= 1
                nums[i], nums[firstTwo] = nums[firstTwo], nums[i]
                i -= 1
            i += 1