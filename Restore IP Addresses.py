"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Restore IP Addresses
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_93
 Notes:
 Given a string containing only digits, restore it by returning all possible valid IP address combinations.
 For example:
 Given "25525511135",
 return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

 Solution: DFS.
 """

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        def validNumber(string):
            if len(string) == 1: return True
            if string[0] != '0' and int(string) <= 255: 
                return True
            return False
        
        def restoreIpAddressesRecur(result, current, i, leftNum):
            if leftNum == 0 and i == len(s):
                result.append(current[1:])
            elif leftNum > 0 :
                for j in xrange(1, 4):
                    if i < len(s) + 1 - j and validNumber(s[i : i + j]):
                        restoreIpAddressesRecur(result, 
                    current + '.' + s[i : i + j], i + j, leftNum - 1)
        result = []
        restoreIpAddressesRecur(result, '', 0, 4)
        return result
                
        