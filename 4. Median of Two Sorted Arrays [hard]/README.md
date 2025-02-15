# Finding the Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, find the median of the two sorted arrays. The overall time complexity should be optimal.

## Solution Approaches
There are two approaches to solving this problem:

### 1. Brute Force Approach (Merging and Sorting)
#### Method
1. Merge `nums1` and `nums2` into a single array.
2. Sort the merged array.
3. If the length of the merged array is odd, return the middle element.
4. If the length is even, return the average of the two middle elements.

#### Code Implementation
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        mergedArrays = nums1 + nums2
        mergedArrays.sort()

        if len(mergedArrays) % 2 != 0:
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
```

#### Complexity Analysis
- **Merging the arrays**: `O(m + n)`
- **Sorting the merged array**: `O((m + n) log (m + n))`
- **Overall Time Complexity**: `O((m + n) log (m + n))`
- **Space Complexity**: `O(m + n)` (for storing the merged array)

#### Drawbacks
- Inefficient for large inputs due to the sorting step.
- Additional space is required to store the merged array.

---

### 2. Optimized Approach (Binary Search)
#### Method
1. Perform binary search on the smaller of the two arrays to minimize time complexity.
2. Partition both arrays such that elements on the left partition are always smaller than elements on the right.
3. Find the correct partition where the max left element is less than or equal to the min right element.
4. Compute the median based on the total number of elements.

#### Code Implementation
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]

            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2.0
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1

solution = Solution()
nums1 = [1,2]
nums2 = [3,4]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
```

#### Complexity Analysis
- **Binary Search Complexity**: `O(log(min(m, n)))`
- **Overall Time Complexity**: `O(log(min(m, n)))`
- **Space Complexity**: `O(1)`, since no additional space is used.

#### Advantages
- **More efficient** than the brute force approach, especially for large inputs.
- **No additional space required** for storing the merged array.
- **Handles edge cases efficiently**, including arrays with different sizes and all elements in one array being smaller or larger than the other.

## Conclusion
| Approach | Time Complexity | Space Complexity | Efficiency |
|----------|----------------|------------------|------------|
| Brute Force (Sorting) | `O((m + n) log (m + n))` | `O(m + n)` | Inefficient for large inputs |
| Optimized (Binary Search) | `O(log(min(m, n)))` | `O(1)` | Best for large inputs |

The binary search approach is the optimal solution due to its logarithmic time complexity and in-place computation. The brute force method, while simpler, becomes impractical for large datasets.

---
**Author:** Muhammad Rezki Ananda

