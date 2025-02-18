# Palindrome Number - LeetCode Solution

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number that reads the same forward and backward.

### Example 1:
**Input:** `x = 121`
**Output:** `true`

### Example 2:
**Input:** `x = -121`
**Output:** `false`

### Example 3:
**Input:** `x = 10`
**Output:** `false`

## Solution
### Approach 1: Convert to String (Current Implementation)
```python
class Solution(object):
    def isPalindrome(self, x):
        res = list(str(x))
        res.reverse()
        return str(x) == "".join(res)
```
**Explanation:**
- Convert the integer to a string.
- Reverse the string and compare it with the original.

**Time Complexity:** O(n) (where n is the number of digits in `x`)
**Space Complexity:** O(n) (since we store the reversed string)

---

## Alternative Approaches

### Approach 2: Two-Pointer Technique
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
```
**Explanation:**
- Use two pointers: one starting from the left and another from the right.
- Compare the characters while moving towards the center.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

### Approach 3: Reverse Half of the Number (Optimal)
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10
```
**Explanation:**
- Handle negative numbers and numbers ending in 0 (except 0 itself).
- Reverse only half of the number.
- Compare the original half with the reversed half.

**Time Complexity:** O(log n) (since we process half the digits)
**Space Complexity:** O(1)

## Insights
1. **String-based solutions** are simple but require extra space.
2. **Two-pointer method** avoids extra space but still operates in O(n) time.
3. **Reversing half the number** is the most optimal approach, reducing time complexity to O(log n) and using O(1) space.

For large numbers, the third approach is recommended since it optimally utilizes memory and performance.

