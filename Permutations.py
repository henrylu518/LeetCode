"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 13, 2015
 Problem:    Permutations
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_46
 Notes:
 Given a collection of numbers, return all possible permutations.
 For example,
 [1,2,3] have the following permutations:
 [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

 Solution: dfs...
 """


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        def permuteLeftWith(result, current, numsLeft):
            if len(numsLeft) == 0: 
                result.append(current)
                return
            for i in xrange(len(numsLeft)):
                permuteLeftWith(result, current + [numsLeft[i]], \
                numsLeft[:i] + numsLeft[i + 1:])
                    
        result = []
        permuteLeftWith(result, [], nums)
        return result

    def permute(self, nums):
        
        def permuteRecur(current, numsLeft):
            if numsLeft == [] : return [current]
            result = []
            for i in xrange(len(numsLeft)):
                result += permuteRecur(current + [numsLeft[i]], 
                    numsLeft[:i] + numsLeft[i + 1:])
            return result

        return permuteRecur([], nums)