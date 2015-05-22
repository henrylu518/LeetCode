"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 21, 2015
 Problem:    Subsets II
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_90
 Notes:
 Given a collection of integers that might contain duplicates, S, return all possible subsets.
 Note:
 Elements in a subset must be in non-descending order.
 The solution set must not contain duplicate subsets.
 For example,
 If S = [1,2,2], a solution is:
 [
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
 ]

 Solution: (2) is use DFS like subset I, just check for the duplicate when add to the result.
            but there is a lot of duplicate work if there is lots of duplicate nums. 
            for example [1] * 30

            (1) For example, S = [1, 2, 2, 4,4,4,4]
            arrangedNums =  [[[], [1]]  [[], [2], [2, 2]], 
            [ [],[4],[4,4], [4,4,4], [4,4,4,4] ] ]
            Then do a multiply.

 """


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        arrangedNums = []
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                arrangedNums[-1].append(arrangedNums[-1][-1] + [nums[i]])
            else:
                arrangedNums.append([[], [nums[i]]])
        current = [[]]
        for i in xrange(len(arrangedNums)):
            next = []
            for e1 in current:
                for e2 in arrangedNums[i]:
                    next.append(e1 + e2)
            current = next
        return current


    def subsetsWithDup_2(self, S):
        results = []
        self.subsetsRecur(results, [], sorted(S))
        return results
    
    def subsetsRecur(self, results, result, S):
        if len(S) == 0 and result not in results:
            results.append(result)
        elif len(S):
            self.subsetsRecur(results, result, S[1:])
            self.subsetsRecur(results, result + [S[0]], S[1:])