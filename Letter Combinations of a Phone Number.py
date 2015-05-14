"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Letter Combinations of a Phone Number
 Difficulty: Medium
 Source:     http://leetcode.com/onlinejudge#question_17
 Notes:
 Given a digit string, return all possible letter combinations that the number could represent.
 A mapping of digit to letters (just like on the telephone buttons) is given below.
 Input:Digit string "23"
 Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 Note:
 Although the above answer is in lexicographical order, your answer could be in any order you want.

 Solution: DFS
 """

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        lookup = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        def letterCombinationsRecur(result, current, leftDigits):
            if leftDigits:
                for char in lookup[int(leftDigits[0])]:
                    letterCombinationsRecur(result, current + char, leftDigits[1:])
            else:
                result.append(current)
        
        if digits == "": return []
        result = []
        letterCombinationsRecur(result, '', digits)
        return result