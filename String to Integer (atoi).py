"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 6, 2015
 Problem:    String to Integer (atoi)
 Difficulty: Easy
 Source:     https://oj.leetcode.com/problems/string-to-integer-atoi/solution/
 Notes:
 Implement atoi to convert a string to an integer.
 Hint: Carefully consider all possible input cases. If you want a challenge, please do not 
 see below and ask yourself what are the possible input cases.
 Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
 You are responsible to gather all the input requirements up front.

 Requirements for atoi:
 The function first discards as many whitespace characters as necessary until the first 
 non-whitespace character is found. Then, starting from this character, takes an optional
 initial plus or minus sign followed by as many numerical digits as possible, and interprets 
 them as a numerical value.
 The string can contain additional characters after those that form the integral number, which 
 are ignored and have no effect on the behavior of this function.
 If the first sequence of non-whitespace characters in str is not a valid integral number, or 
 if no such sequence exists because either str is empty or it contains only whitespace characters, 
 no conversion is performed.
 If no valid conversion could be performed, a zero value is returned. If the correct value is out 
 of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

 Solution: 1. use a index point to go through the input str (use a while loop)  
                (always remember to check the index bound when access member in array)
           2. use a for-in loop to go through the input str
           because each element of the input str are highly related. 
           The use of later element is conditioned on the early element. 
           In this situation, it is not suitable to use the for-in loop, 
            or it will end up with a lot of if-else conditions. 
            The code will be very hard to read and it is very easy to forget one condition.
 In python , the integer value is automatical change to long if the integer is overflow
 In other languge, 1. could use long to avoid overflow and check if there is overflow for the int32
                   2. don't use the long. check the current value is bigger to INT_MAX / 10, 
                    or current value equal to INT_MAX / 10, 
                    the char value >= INT_MAX % 10 or INT_MIN % 10  based on the sign
"""


class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi_1(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if not str: return 0
        point = 0
        while point < len(str) and str[point] == " ": point += 1
        positive = True
        if point < len(str) and str[point] in "+-":
            positive = (str[point] == "+")
            point += 1
        result = 0
        while point < len(str) and str[point].isdigit():
            result = result * 10 + int(str[point])
            point += 1
        result = result if positive else -result
        if result > INT_MAX:  return INT_MAX
        if result < INT_MIN:  return INT_MIN
        return result


    def myAtoi_2(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        optionalSign = None
        resultInt = None
        if str == "":
            return 0
        for char in str:
            if char.isdigit():
                if resultInt == None:
                    resultInt = int(char)
                else:
                    resultInt = resultInt * 10 + int(char)
                    if resultInt > INT_MAX and optionalSign != -1:
                        resultInt = INT_MAX
                    elif resultInt > -INT_MIN and optionalSign == -1:
                        resultInt = -INT_MIN
            else:
                if resultInt == None:
                    if optionalSign == None:
                        if char == "+":
                            optionalSign = 1
                        elif char == "-":
                            optionalSign = -1
                        elif char == " ":
                            continue
                        else:
                            break
                    else:
                        break
                else:
                    break
        if resultInt == None:
            return 0
        return resultInt * optionalSign if optionalSign != None else resultInt

