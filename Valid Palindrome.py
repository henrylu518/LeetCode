class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while j > i:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1  
        return True