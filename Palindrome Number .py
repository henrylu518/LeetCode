"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 16, 2015
 Problem:    Palindrome Number
 Difficulty: Easy
 Source:     http://leetcode.com/onlinejudge#question_9
 Notes:
 Determine whether an integer is a palindrome. Do this without extra space.
 Some hints:
 Could negative integers be palindromes? (ie, -1) (No!)
 If you are thinking of converting the integer to string, note the restriction of using extra space.
 You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
 you know that the reversed integer might overflow. How would you handle such case?
 There is a more generic way of solving this problem.

 Solution:  Reverse the number, then check to see if x == reverse(x).
 """

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        def reverse(x):
            num = 0
            while x:
                lastDigit = x % 10
                num = 10 * num + lastDigit
                x = x / 10
            return num
        if x < 0: return False
        return reverse(x) == x

    # def isPalindrome(self, x):
    #     def reverse(x):
    #         num, sign = 0, 1
    #         if x < 0:
    #             sign, x = -1, -x
    #         while x:
    #             lastDigit = x % 10
    #             num = 10 * num + lastDigit
    #             x = x / 10
    #         return num
        
    #     return reverse(x) == x