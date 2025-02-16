class Solution(object):
    def _reverse(self, x): # 16ms
        sign = 1
        if x < 0:
            sign = -1

        result = int(str(abs(x))[::-1]) * sign

        upper32bit = 2**31 -1
        lower32bit = -2**31

        if result < lower32bit or result > upper32bit:
            return 0

        return result

    def reverse(self, x):
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            result = result * 10 + x % 10
            x //= 10

        result *= sign

        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0

        return result




solution = Solution()
data = 12345
result = solution.reverse(data)
print(result)