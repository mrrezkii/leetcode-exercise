# Container With Most Water - LeetCode Solution

## Problem Statement
Given an integer array `height` where `height[i]` represents the height of a vertical line at index `i`, the task is to find two lines that together with the x-axis form a container, such that the container holds the maximum amount of water.

**Constraints:**
- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`

## Approach: Two-Pointer Technique

### Code Implementation
```python
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
```

### Explanation
The two-pointer approach is used to solve this problem efficiently:
1. **Initialize Two Pointers:**
   - `left` at the beginning of the array (index 0)
   - `right` at the end of the array (index `n-1`)

2. **Calculate Area:**
   - Compute the container area using `min(height[left], height[right]) * (right - left)`
   - Update `res` if this area is the maximum found so far

3. **Move the Pointers:**
   - Move the pointer that is pointing to the shorter line, since increasing the width while keeping the shorter height does not improve the maximum area.

4. **Repeat Until Pointers Meet:**
   - The loop continues until `left` and `right` meet.

### Time Complexity Analysis
- The algorithm runs in **O(n)** time because each iteration either increments `left` or decrements `right`, leading to at most `n` iterations.
- Space complexity is **O(1)** as no additional data structures are used.

## Comparison with the Best Approach
Your approach is already optimal. However, let’s compare it to a brute-force approach and understand why the two-pointer technique is the best.

### 1. **Brute Force Approach** (Inefficient)
#### Code:
```python
class Solution:
    def maxArea(self, height):
        n = len(height)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                container = min(height[i], height[j]) * (j - i)
                res = max(res, container)
        return res
```

#### Complexity Analysis:
- **Time Complexity: O(n^2)** since it checks all pairs `(i, j)`, making it extremely slow for large `n`.
- **Space Complexity: O(1)** (no extra space is used).

### 2. **Optimized Two-Pointer Approach** (Best Solution - Same as Your Approach)
- **Time Complexity: O(n)** as each pointer moves at most `n` times.
- **Space Complexity: O(1)**.

### Why Two-Pointer Works Better
- Instead of checking every pair, it uses a **greedy shrinking strategy** where we always move the smaller height.
- This ensures that we have the best chance of increasing the maximum area by keeping the taller side and reducing width in a controlled manner.

## Conclusion
- Your solution using the **two-pointer technique** is the optimal approach with **O(n) time complexity**.
- The brute-force approach is impractical due to **O(n²) complexity**.
- **Key takeaway:** Always try to use a **two-pointer approach** in problems that involve **finding an optimal pair in a sorted-like order**.

This solution efficiently finds the maximum water container with minimal computations, making it the best approach for the problem.

