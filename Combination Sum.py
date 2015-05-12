class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        
        def combinationSumRecur(result, current, remainCandidates, leftVal):
            if leftVal == 0:  result.append(current); return
            if leftVal < 0 or remainCandidates == []: return
            candidate = remainCandidates[-1]
            combinationSumRecur(result, [candidate] + current, remainCandidates, leftVal - candidate)
            combinationSumRecur(result, current, remainCandidates[:-1], leftVal)

        
        candidates = sorted(list(candidates))
        result = []
        combinationSumRecur(result, [], candidates, target)
        return result