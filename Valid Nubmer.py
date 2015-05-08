"""
 Author:     Henry, henrylu518@gmail.com 
 Date:       May 8, 2015
 Problem:    Valid Number
 Difficulty: Hard
 Source:     https://oj.leetcode.com/problems/valid-number/
 Notes:
 Validate if a given string is numeric.
 Some examples:
 "0" => true
 " 0.1 " => true
 "abc" => false
 "1 a" => false
 "2e10" => true
 Note: It is intended for the problem statement to be ambiguous. You should gather all 
 requirements up front before implementing one.


specical char:  "e", ".", "+", "-"
" 005047e+6", " -.5 ", " .2e+6", " 2.34e2 " : True
"e10", "2e2.8", ".", " ", "6+2" : False

1. check " "     (while)
2. check "+", "-"  (if)
3. check digit   (while)
4. check "."  (elif)
	check digit (while)
5. check "e"   (if)
	before "e": there should be digits
	must:	(1) : check "+", "-" (if)
			(2) : check digit (while)
6. check " "  (while)
7. return (check if reach the end) and (there is digit)

" " is not a False, "" is a False
Could not combine step4 and step5 check digit, because of " 2.34e2 "
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        i = 0
        sLen = len(s)
        digitBegin = False
        while i < sLen and s[i] == " ": i += 1
        if i < sLen and s[i] in "+-":
            i += 1
        while i < sLen and s[i].isdigit(): i += 1; digitBegin = True
        if i < sLen and s[i] == ".":	
        	i += 1
        	while i < sLen and s[i].isdigit(): i += 1; digitBegin = True
        if i < sLen - 1 and digitBegin and s[i] == "e" :
            i += 1
            digitBegin = False
            if s[i] in "+-":  i += 1
            while i < sLen and s[i].isdigit(): i += 1; digitBegin = True
        while i < sLen and s[i] == " ": i += 1
        return i == sLen and digitBegin
