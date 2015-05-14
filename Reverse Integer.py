"""
 Author:    Henry, henrylu518@gmail.com
 Date:       May 14, 2015
 Problem:    Reverse Integer
 Difficulty: Easy
 Source:     https://oj.leetcode.com/problems/reverse-integer/
 Notes:
 Reverse digits of an integer.
 Example1: x = 123, return 321
 Example2: x = -123, return -321

 Have you thought about this?
 Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
 If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
 Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
 Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the function (ie, add an extra parameter).

 Solution: Use % and / iteratively.
 """

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        y = 0
        while x:
            y = 10*y + x % 10
            x /= 10
        if y > 2 ** 31: return 0
        return sign * y