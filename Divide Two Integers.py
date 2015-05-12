

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        maxINT, minINT = 2147483647, -2147483648
        if divisor == 0: return maxINT
        positive = True
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            positive = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        times, divisorTimes = [1], [divisor]
        while divisorTimes[-1] <= dividend:
            times.append(times[-1] + times[-1])
            divisorTimes.append(divisorTimes[-1] + divisorTimes[-1])
        i, j = 0, -1
        while dividend >= divisor:
            if dividend >= divisorTimes[j]:
                dividend -= divisorTimes[j]
                i += times[j]
            j -= 1
        if not positive: i = -i 
        if i > maxINT or i < minINT:    return maxINT
        return i

