class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        closestDiff, closest = float("Inf"), None
        i, nums = 0, sorted(nums)
        for i in xrange(len(nums)):
            k, l = i + 1, len(nums) - 1
            remainTarget = target - nums[i]
            while k < l:
                twoSum = nums[k] + nums[l]
                diff = abs(twoSum - remainTarget)
                if diff < closestDiff:
                    closestDiff = diff
                    closest = nums[i] + twoSum
                if twoSum > remainTarget:
                    l -= 1
                elif twoSum < remainTarget:
                    k += 1
                else:
                    return target
        return closest