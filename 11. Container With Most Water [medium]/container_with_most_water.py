class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            container = min(height[left], height[right]) * (right - left)
            res = max(res, container)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

solution = Solution()
data = [2, 1, 8, 6, 4, 6, 5, 5]
result = solution.maxArea(data)
print(result)