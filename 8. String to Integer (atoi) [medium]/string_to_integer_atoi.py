class Solution(object):
    def myAtoi(self, s):
        sTrim = s.strip()
        digits = ""
        for i in range(len(sTrim)):
            if i == 0 and ("-" == sTrim[i] or "+" == sTrim[i]):
               digits += sTrim[i]
            elif sTrim[i].isnumeric():
                digits += sTrim[i]
            else:
                break

        if digits == "" or digits == "-" or digits == "+":
            return 0

        result = int("".join(digits))

        up = 2 ** 31 - 1
        if result > up:
            return up

        low = -2 ** 31
        if result < low:
            return low

        return result





solution = Solution()
data = "21474836460"
result = solution.myAtoi(data)
print(result)