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