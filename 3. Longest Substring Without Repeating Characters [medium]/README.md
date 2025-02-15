# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the **length** of the **longest substring** without repeating characters.

## Examples

### Example 1
**Input:**  
`s = "abcabcbb"`

**Output:**  
`3`  
**Explanation:** The longest substring is `"abc"`, which has a length of `3`.

---

### Example 2
**Input:**  
`s = "bbbbb"`

**Output:**  
`1`  
**Explanation:** The longest substring is `"b"`, which has a length of `1`.

---

### Example 3
**Input:**  
`s = "pwwkew"`

**Output:**  
`3`  
**Explanation:** The longest substring is `"wke"`, which has a length of `3`.

---

## Approach: Sliding Window

We use the **sliding window** technique to efficiently find the longest substring.

### Steps:
1. Use a **set** to store unique characters in the current window.
2. Use **two pointers** (`left` and `right`) to define the current substring.
3. Expand the window by moving the **right pointer** until a duplicate character is found.
4. If a duplicate exists, move the **left pointer** forward until all characters in the window are unique again.
5. Track the **maximum length** of such a window.

---

## Solution Implementation

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # To store unique characters in the window
    left = 0  # Left pointer of the window
    max_length = 0  # Maximum length of substring
    
    # Move the right pointer to expand the window
    for right in range(len(s)):
        while s[right] in char_set:
            # Remove leftmost character until no duplicate
            char_set.remove(s[left])
            left += 1  # Move left pointer
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update max_length
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

---

## Example Walkthrough

### Input: `s = "abcabcbb"`

| Step | Left | Right | Window (`s[left:right+1]`) | Set (`char_set`) | Max Length |
|------|------|------|--------------------------|------------------|------------|
| 1    | 0    | 0    | `"a"`                    | `{'a'}`          | 1          |
| 2    | 0    | 1    | `"ab"`                   | `{'a', 'b'}`     | 2          |
| 3    | 0    | 2    | `"abc"`                  | `{'a', 'b', 'c'}`| 3          |
| 4    | 0    | 3    | `"abca"` (Duplicate)     | Remove `'a'`, Move `left=1` |
| 5    | 1    | 3    | `"bca"`                  | `{'b', 'c', 'a'}`| 3          |
| 6    | 1    | 4    | `"bcab"` (Duplicate)     | Remove `'b'`, Move `left=2` |
| 7    | 2    | 4    | `"cab"`                  | `{'c', 'a', 'b'}`| 3          |

**Final Output:** `3`

---

## Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the length of `s`. We traverse `s` once using the right pointer and move the left pointer as needed.
- **Space Complexity:** `O(min(n, 26)) ≈ O(1)`, since the set stores at most `26` unique characters.

---

## Alternative Approaches

### Using a Dictionary (Character Index Map)
Instead of using a set, we can use a dictionary to store the index of characters:

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # Stores the last seen index of each character
    left = 0  # Left boundary of the window
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  # Move left past the repeated character
        
        char_index[s[right]] = right  # Update last seen index
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

This approach is similar but more efficient in some cases as it avoids unnecessary `while` loops.

---

## Summary
- **Sliding Window** is the best approach.
- **Time Complexity is O(n)**.
- We can use either **set or dictionary** for tracking characters.
- Useful for solving similar **substring problems**.

