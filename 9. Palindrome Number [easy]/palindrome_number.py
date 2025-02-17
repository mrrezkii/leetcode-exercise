class Solution(object):
    def isPalindrome(self, x):
        res = list(str(x))
        res.reverse()

        if str(x) == "".join(res):
            return True

        return False

solution = Solution()
data = 121
result = solution.isPalindrome(data)
print(result)