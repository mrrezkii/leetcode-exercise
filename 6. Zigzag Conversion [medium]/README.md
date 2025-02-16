# Zigzag Conversion Solution

## Problem Statement
The **Zigzag Conversion** problem is from LeetCode (#6). The task is to convert a given string `s` into a zigzag pattern on a given number of rows `numRows` and then read it row by row.

### Example 1
**Input:**
```plaintext
s = "PAYPALISHIRING", numRows = 3
```
**Zigzag Pattern:**
```plaintext
P   A   H   N
A P L S I I G
Y   I   R
```
**Output:**
```plaintext
"PAHNAPLSIIGYIR"
```

### Example 2
**Input:**
```plaintext
s = "PAYPALISHIRING", numRows = 4
```
**Zigzag Pattern:**
```plaintext
P     I    N
A   L S  I G
Y A   H R
P     I
```
**Output:**
```plaintext
"PINALSIGYAHRPI"
```

---

## Approach
We follow these steps to solve the problem efficiently:
1. **Edge Cases:** If `numRows == 1` or `numRows >= len(s)`, return `s` directly since no zigzag conversion is needed.
2. **Create a list of strings** for each row (`rows` list of size `numRows`).
3. **Iterate through the string `s`**, adding each character to the corresponding row based on the zigzag traversal.
4. **Use a direction flag (`step`)** to move downward until reaching the last row, then switch direction to move upward.
5. **Join all rows** to create the final output string.

### Time Complexity
- **O(n)**: We iterate through the string once and join the result, making it efficient.

---

## Code Implementation (Python)
```python
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = ["" for _ in range(numRows)]  # Create an empty list for each row
    index, step = 0, 1  # Index tracks the current row, step determines direction

    for char in s:
        rows[index] += char  # Append character to the current row
        
        # Change direction at the first and last rows
        if index == 0:
            step = 1  # Move down
        elif index == numRows - 1:
            step = -1  # Move up
        
        index += step  # Update the row index

    return "".join(rows)  # Combine all rows into a single string

# Example usage
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
```

---

## Explanation of the Code
1. **Handle Edge Cases:** If `numRows` is 1 or larger than the string length, return `s` directly.
2. **Create a list of empty strings** (`rows`), one for each row.
3. **Use an index to track the row position** and a `step` variable to control direction.
4. **Iterate through `s` and populate the `rows` list** by appending characters accordingly.
5. **Adjust the direction** when reaching the first (`index == 0`) or last (`index == numRows - 1`) row.
6. **Join all rows** to form the final zigzag converted string.

---

## Alternative Approaches
1. **Using 2D Arrays:**
   - We can simulate a matrix and place characters accordingly, then extract the rows.
   - **Downside:** Higher space complexity.
   
2. **Using StringBuilder (Java) or `StringBuilder.append()` in Python:**
   - Instead of list concatenation, we use `StringBuilder` to optimize string operations.
   
---

## Edge Cases Considered
- `numRows = 1` (No zigzag conversion needed)
- `numRows >= len(s)` (No transformation required)
- Short strings (e.g., `s = "A"`, `numRows = 5`)
- Large input strings (Performance testing)

---

## Conclusion
This approach efficiently converts a given string into its zigzag form using an optimized traversal method. With a time complexity of **O(n)**, it provides a scalable solution even for large input sizes.

