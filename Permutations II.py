"""
 Date:       May 18, 2015
 Problem:    Permutations II
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_47
 Notes:
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.
 For example,
 [1,1,2] have the following unique permutations:
 [1,1,2], [1,2,1], and [2,1,1].

 Solution: dfs...
 """

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        def permuteRecur(result,current, numsLeft):
            if numsLeft == []:
                result.add(tuple(current))
                return
            i = 0
            while i < len(numsLeft):
                if i > 0 and numsLeft[i - 1] == numsLeft[i]:
                    i += 1
                    continue
                permuteRecur(result, current + [numsLeft[i]], numsLeft[:i] + numsLeft[i + 1:])
                i += 1
        
        
        result = set()
        permuteRecur(result, [], sorted(nums))
        return [list(e) for e in result]
print Solution().permuteUnique([1,1,2])