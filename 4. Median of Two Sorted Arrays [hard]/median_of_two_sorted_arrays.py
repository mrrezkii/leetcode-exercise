class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2): #4ms
        mergedArrays = nums1 + nums2
        mergedArrays.sort()

        if len(mergedArrays) %2 != 0:
            median = len(mergedArrays) // 2
            return mergedArrays[median]

        left = len(mergedArrays) // 2 - 1
        right = left + 1
        return float(mergedArrays[left] + mergedArrays[right]) / 2


solution = Solution()
nums1 = [1,2]
nums2 = [3,4]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)