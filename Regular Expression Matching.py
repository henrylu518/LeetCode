"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 12, 2015
 Problem:    Regular Expression Matching
 Difficulty: Hard
 Source:     http://leetcode.com/onlinejudge#question_10
 Notes:
 Implement regular expression matching with support for '.' and '*'.
 '.' Matches any single character.
 '*' Matches zero or more of the preceding element.
 The matching should cover the entire input string (not partial).
 The function prototype should be:
 bool isMatch(const char *s, const char *p)
 Some examples:
 isMatch("aa","a") ? false
 isMatch("aa","aa") ? true
 isMatch("aaa","aa") ? false
 isMatch("aa", "a*") ? true
 isMatch("aa", ".*") ? true
 isMatch("ab", ".*") ? true
 isMatch("aab", "c*a*b") ? true

 Solution: Both of the two solutions are the same. Just re-organize the code. 
            Solution_2 is much easy to read.
 The reason why there is a pre-process of the p is for the case of 
 isMatch("aaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*b*b*b*c")
"""

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    
    def isCharMatch(self, c1, c2):
        if c2 == ".": return True
        return c1 == c2
    
    def isMatchRecur(self, s, p):
            if len(s) == 0 and len(p) == 0: return True
            if len(s) != 0 and len(p) == 0: return False
            if len(p) > 1 and p[1] == "*":
                if s == "":
                    return self.isMatchRecur(s, p[2:])
                if self.isCharMatch(s[0], p[0]): 
                    return self.isMatchRecur(s, p[2:]) or self.isMatchRecur(s[1:], p)
                else:
                    return self.isMatchRecur(s, p[2:]) 
            else:
                if s == "": return False
                if self.isCharMatch(s[0], p[0]): 
                    return self.isMatchRecur(s[1:], p[1:])
                else:
                    return False


    def isMatch(self, s, p):
        i, pLen, p1 = 0, len(p), ""
        while i < pLen :
            if i < pLen - 3 and p[i: i + 2] == p[i + 2: i + 4] and p[i + 1] == "*":
                i += 2
            else:
                p1 += p[i]
                i += 1
        return self.isMatchRecur(s, p1)
        


class Solution_2:
    # @param {string} s
    # @param {string} p
    # @return {boolean}

    def isMatchRecur(self, s, p):
        if len(p) == 0: return len(s) == 0
        if s and (s[0] == p[0] or p[0] == '.'):
            if len(p) > 1 and p[1] == "*":
                return self.isMatchRecur(s[1:], p) or self.isMatchRecur(s, p[2:])
            else:
                return self.isMatchRecur(s[1:], p[1:])
        return len(p) > 1 and p[1] == "*" and self.isMatchRecur(s, p[2:])

    def isMatch(self, s, p):
        i, pLen, p1 = 0, len(p), ""
        while i < pLen :
            if i < pLen - 3 and p[i: i + 2] == p[i + 2: i + 4] and p[i + 1] == "*":
                i += 2
            else:
                p1 += p[i]
                i += 1
        return self.isMatchRecur(s, p1)
