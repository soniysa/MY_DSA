class Solution:
    def myAtoi(self, s: str):

        s = s.strip()

        if not s:
            return 0

        sign = 1
        ans = 0
        idx = 0

        # Check sign
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            idx += 1

        # Read digits
        while idx < len(s) and s[idx].isdigit():

            digit = int(s[idx])

            # Overflow check for positive number
            if sign == 1:
                if ans > 2147483647 // 10 or (
                    ans == 2147483647 // 10 and digit > 7
                ):
                    return 2147483647

            # Overflow check for negative number
            else:
                if ans > 2147483648 // 10 or (
                    ans == 2147483648 // 10 and digit > 8
                ):
                    return -2147483648

            ans = ans * 10 + digit
            idx += 1

        return sign * ans