"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Integer to Roman
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_12
 Notes:
 Given an integer, convert it to a roman numeral.
 Input is guaranteed to be within the range from 1 to 3999.

 Solution: Buffer the roman numbers. (4, 9)
 """

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        symbol = {1 : "I", 4 : "IV", 5 : "V", 9 : "IX", \
        10 : "X", 40 : "XL", 50 : "L", 90 : "XC", 100 : "C", \
        400 : "CD", 500 : "D", 900 : "CM", 1000 : "M"}
        reversedSymbolKeys = sorted(symbol.keys(), reverse = True)
        result = ""
        for key in reversedSymbolKeys:
            while num >= key:
                result += symbol[key]
                num -= key
        return result

                             