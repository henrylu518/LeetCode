
        
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def allPalindromeLastWith(j):
            palindromes = []
            for i in xrange(j + 1):
                if isPalindrome(i, j):
                    palindromes.append((i,j))
            return palindromes
       
        sLen = len(s)
        table = []
        for j in xrange(sLen):
            palindromes = allPalindromeLastWith(j)
            table.append([])
            for (start, end) in palindromes:
                if start == 0:
                    table[j].append([(start, end)])
                else:
                    table[j] += [e + [(start, end)] for e in table[start - 1]]  

        result = []

        for onePartition in table[sLen - 1]:
            current = []
            for (start, end) in onePartition:
                current.append(s[start:end + 1])
            result.append(current)
        return result