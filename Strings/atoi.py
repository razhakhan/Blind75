class Solution:
    def myAtoi(self, s):
        sign = 1
        res = 0
        idx = 0
        n = len(s)

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. Skip spaces
        while idx < n and s[idx] == " ":
            idx += 1

        # 2. Sign
        if idx < n and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                sign = -1
            idx += 1

        # 3. Digits
        while idx < n and '0' <= s[idx] <= '9':
            digit = ord(s[idx]) - ord('0')

            # overflow check BEFORE update
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            idx += 1

        return sign * res

'''
Remember: 
1. Always check bounds:
2. You are treating number construction and overflow as two separate phases. Overflow must be checked while building the number digit by digit.

# overflow check formula

Rearrange the condition 

Start with:

res * 10 + digit > INT_MAX


Subtract digit from both sides:

res * 10 > INT_MAX - digit


Divide both sides by 10:

res > (INT_MAX - digit) // 10
'''
