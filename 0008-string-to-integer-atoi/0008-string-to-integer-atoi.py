class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if not s :
            return 0

        sign = 1
        ans = 0
        idx = 0 
 
        if s[0] == '-' or s[0] == '+' :
            if s[0] == '-' :
                sign = -1
            idx+=1

        while idx < len(s) and s[idx].isdigit():
            digit = int(s[idx])

            if sign == 1 and (
                ans > 2147483647 // 10 or
                (ans == 2147483647 // 10 and digit > 7)
            ):
                return 2147483647
            
            if sign == -1 and (
                ans > 2147483648 // 10 or
                (ans == 2147483648 // 10 and digit > 8)
            ):
                return -2147483648
            
            ans = ans * 10 + digit 
            idx += 1

        return sign * ans
        