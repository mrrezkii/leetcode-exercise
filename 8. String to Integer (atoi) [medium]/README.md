# String to Integer (atoi)

## Problem Statement
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to the `atoi` function in C/C++). The function follows these rules:

1. Ignore leading whitespace.
2. Consider an optional `+` or `-` sign.
3. Read digits until a non-digit character is encountered.
4. If no digits are found, return `0`.
5. Clamp the result to fit in a signed 32-bit integer range `[-2^31, 2^31 - 1]`.
6. Return the final integer value.

---

## Implementation
The following Python implementation follows the steps described in the problem statement:

```python
class Solution(object):
    def myAtoi(self, s):
        sTrim = s.strip()
        digits = ""
        for i in range(len(sTrim)):
            if i == 0 and ("-" == sTrim[i] or "+" == sTrim[i]):
                digits += sTrim[i]
            elif sTrim[i].isnumeric():
                digits += sTrim[i]
            else:
                break

        if digits == "" or digits == "-" or digits == "+":
            return 0

        result = int("".join(digits))

        up = 2 ** 31 - 1
        if result > up:
            return up

        low = -2 ** 31
        if result < low:
            return low

        return result
```

---

## Alternative Approach
While the above solution works, it can be improved in terms of efficiency and readability. Below is an optimized approach using a more structured approach with `re` (regular expressions):

```python
import re

class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()  # Remove leading whitespaces
        match = re.match(r'^[+-]?\d+', s)  # Use regex to extract a valid number
        if not match:
            return 0
        
        num = int(match.group())
        
        # Clamping within 32-bit signed integer range
        return max(min(num, 2**31 - 1), -2**31)
```

### Why is this approach better?
1. **Efficiency**: Uses `re.match()` to extract the valid integer part in one go, rather than iterating character by character.
2. **Readability**: The code is cleaner and easier to understand.
3. **Edge-case handling**: Avoids manual checks for empty or invalid strings.

---

## Complexity Analysis
| Approach        | Time Complexity | Space Complexity |
|---------------|---------------|---------------|
| Original Solution | O(N) | O(1) |
| Regex Solution   | O(N) | O(1) |

Both approaches have the same time complexity, but the regex approach simplifies the logic.

---

## Edge Cases Considered
- Strings with only whitespace (`"  "`) → Returns `0`
- Strings with non-numeric characters before numbers (`"words and 987"`) → Returns `0`
- Strings with mixed valid and invalid characters (`"-91283472332abc"`) → Parses `-91283472332`, then clamps to `-2^31`.
- Strings with only `"+"` or `"-"` → Returns `0`.

---

## Conclusion
This problem teaches parsing logic, handling edge cases, and working with integer constraints. The regex-based approach is cleaner and recommended for production code, while the iterative approach provides more control over each parsing step.

