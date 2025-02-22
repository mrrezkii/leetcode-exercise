# Integer to Roman Conversion

## Problem Statement
Given an integer, convert it to a Roman numeral. Roman numerals are represented by the following symbols:

| Symbol | Value |
|--------|-------|
| M      | 1000  |
| CM     | 900   |
| D      | 500   |
| CD     | 400   |
| C      | 100   |
| XC     | 90    |
| L      | 50    |
| XL     | 40    |
| X      | 10    |
| IX     | 9     |
| V      | 5     |
| IV     | 4     |
| I      | 1     |

## Solution 1: Using Ordered Dictionary (Greedy Approach)

### Implementation
```python
from collections import OrderedDict

class Solution(object):
    def intToRoman(self, num):
        romans = OrderedDict([
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ])
        
        result = ""
        for key, value in romans.items():
            d, num = divmod(num, key)
            result += value * d
        return result
```
### Explanation
1. We define an ordered dictionary with integer-to-Roman mappings in descending order.
2. We iterate through the dictionary, checking how many times each Roman numeral fits into the given number.
3. We append the corresponding Roman numeral and reduce the number accordingly.
4. We return the final Roman numeral representation.

### Complexity Analysis
- **Time Complexity**: O(1) – Since the number of Roman numeral symbols is fixed, the loop always iterates over 13 elements at most.
- **Space Complexity**: O(1) – We use a fixed dictionary and a result string.

---

## Alternative Approaches

### Solution 2: Using List of Tuples (Similar to OrderedDict but More Compact)
```python
class Solution:
    def intToRoman(self, num):
        romans = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = ""
        for value, symbol in romans:
            while num >= value:
                result += symbol
                num -= value
        return result
```

### Explanation
- Similar to the ordered dictionary approach but uses a list of tuples instead.
- Instead of `divmod`, we use a `while` loop to subtract the largest possible values.

### Complexity Analysis
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

---

### Solution 3: Using Recursion
```python
class Solution:
    def intToRoman(self, num):
        romans = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        if num == 0:
            return ""
        for value, symbol in romans:
            if num >= value:
                return symbol + self.intToRoman(num - value)
```

### Explanation
- This approach recursively reduces the integer by the largest possible Roman numeral value at each step.
- It stops when `num` reaches zero.

### Complexity Analysis
- **Time Complexity**: O(1), as the recursive depth is bounded by the number of Roman numeral symbols.
- **Space Complexity**: O(1), but recursive calls increase stack usage.

---

## Summary of Approaches
| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Ordered Dictionary | O(1) | O(1) | Uses `OrderedDict` for clean mapping |
| List of Tuples | O(1) | O(1) | More compact, avoids `OrderedDict` |
| Recursion | O(1) | O(1) (but increased stack usage) | Simple but less efficient due to function calls |

Each approach has its own advantages. The first and second methods are more efficient, while the recursive method is more intuitive but has additional function call overhead.

---

## References
- [LeetCode - Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

