class Solution(object):
    def _twoSum(self, nums, target): #   2010ms -> O(N²)
        for i in range(len(nums)):
            for j in range(i + 1):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

    def twoSum(self, nums, target):
        map = dict() # 29ms -> O(N)
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in map:
                return [map.get(complement), i]

            map[nums[i]] = i

        return [0,0]



solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)