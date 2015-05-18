"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 18, 2015
 Problem:    Combination Sum II
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_40
 Notes:
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations
 in C where the candidate numbers sums to T.
 Each number in C may only be used once in the combination.
 Note:
 All numbers (including target) will be positive integers.
 Elements in a combination (a1, a2, .. , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
 The solution set must not contain duplicate combinations.
 For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
 A solution set is: 
 [1, 7] 
 [1, 2, 5] 
 [2, 6] 
 [1, 1, 6] 

 Solution: 
 """

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        
        def combinationSumRecur(result, current, start, leftTarget):
            if leftTarget == 0:
                result.append(current)
                return
            if start < len(candidates) and candidates[start] <= leftTarget:
                combinationSumRecur(result, current + [candidates[start]],
                start + 1, leftTarget - candidates[start])
                while start < len(candidates) - 1 and candidates[start + 1] == candidates[start]:
                    start += 1
                combinationSumRecur(result, current, start + 1, leftTarget)
        
        result = []
        candidates = sorted(candidates)
        combinationSumRecur(result, [], 0, target)
        return result

        