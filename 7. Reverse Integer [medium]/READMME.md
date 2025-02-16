# Reverse Integer - LeetCode Solution

## Problem Statement
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, return `0`.

## Initial Solution (Using String Conversion)
```python
class Solution(object):
    def reverse(self, x):
        sign = 1 if x >= 0 else -1  # Determine the sign
        result = int(str(abs(x))[::-1]) * sign  # Convert to string, reverse, and restore sign

        if result < -2**31 or result > 2**31 - 1:  # Check 32-bit limit
            return 0
        return result
```

### Pros:
✅ Simple and easy to understand
✅ Utilizes Python’s built-in string manipulation capabilities

### Cons:
❌ **String conversion is inefficient**: Converting an integer to a string and back adds unnecessary overhead.
❌ **Extra memory usage**: Strings take additional space, which is inefficient for large numbers.
❌ **Slower execution**: String operations like slicing (`[::-1]`) are not as fast as direct mathematical operations.

## Optimized Solution (Using Mathematics)
```python
class Solution(object):
    def reverse(self, x):
        result = 0
        sign = -1 if x < 0 else 1  # Determine the sign
        x = abs(x)  # Work with the absolute value

        while x:
            result = result * 10 + x % 10  # Extract the last digit and add to result
            x //= 10  # Remove the last digit from x

        result *= sign  # Restore the sign

        if result < -2**31 or result > 2**31 - 1:  # Check for overflow
            return 0
        return result
```

### Why This Solution is Better:
✅ **No string conversion**: Avoids unnecessary operations and improves efficiency.
✅ **Lower memory usage**: Works entirely within the integer domain, avoiding extra allocations.
✅ **Faster execution**: Uses basic arithmetic (`%` and `//`), which are much faster than string operations.

### Step-by-Step Explanation (Beginner Friendly)
1. **Determine the sign of `x`**:
   - If `x` is negative, store `-1` in `sign`.
   - Otherwise, store `1`.
   - Convert `x` to its absolute value for easy processing.

2. **Reverse the digits using a mathematical approach**:
   - Initialize `result = 0`.
   - Use a loop to extract the last digit using `x % 10`.
   - Shift `result` to the left (`result * 10`) and add the extracted digit.
   - Remove the last digit from `x` using integer division (`x //= 10`).
   - Repeat until `x` becomes `0`.

3. **Restore the sign of the result** by multiplying it with `sign`.

4. **Check for overflow**:
   - If `result` is outside the range `[-2^31, 2^31 - 1]`, return `0`.

### Example Walkthrough:
#### Input: `x = 123`
#### Steps:
| Step | x    | result |
|------|------|--------|
| 1    | 123  | 0      |
| 2    | 12   | 3      |
| 3    | 1    | 32     |
| 4    | 0    | 321    |
#### Output: `321`

#### Input: `x = -123`
#### Steps:
| Step | x    | result |
|------|------|--------|
| 1    | 123  | 0      |
| 2    | 12   | 3      |
| 3    | 1    | 32     |
| 4    | 0    | 321    |
#### Output: `-321` (after applying `sign = -1`)

## Time & Space Complexity
| Approach         | Time Complexity | Space Complexity |
|-----------------|----------------|-----------------|
| String Method   | O(n)            | O(n)            |
| Math Method     | O(log n)        | O(1)            |

- `n` is the number of digits in `x`.
- The optimized approach is **faster** and **more memory-efficient**.

## Summary
- **Initial solution**: Uses string manipulation (slower, more memory usage).
- **Optimized solution**: Uses mathematical operations (faster, less memory usage).
- **Key takeaways**:
  - Avoid unnecessary string conversions when working with numbers.
  - Mathematical operations are often more efficient.
  - Always check for overflow when dealing with integer constraints.

This solution ensures an efficient and beginner-friendly approach to solving the problem!

