# Longest Palindromic Substring

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

## Approaches to Solve the Problem

### 1. Brute Force (O(n^3))
- Generate all possible substrings.
- Check if each substring is a palindrome.
- Keep track of the longest one.

```python
def longestPalindrome(s: str) -> str:
    def is_palindrome(sub):
        return sub == sub[::-1]

    n = len(s)
    max_length = 0
    longest_substring = ""

    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j + 1]) and (j - i + 1) > max_length:
                max_length = j - i + 1
                longest_substring = s[i:j + 1]
    
    return longest_substring
```

### 2. Expand Around Center (O(n^2))
- Consider each character (or pair) as a potential center.
- Expand outward while valid.

```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    
    return longest
```

### 3. Dynamic Programming (O(n^2))
- Use a DP table to track palindrome validity.

```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_length = i, 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_length = i, length

    return s[start:start + max_length]
```

### 4. Manacher’s Algorithm (O(n))
- Best approach for large inputs.
- Uses a transformed string to handle even-length palindromes.

```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    T = '#' + '#'.join(s) + '#'
    n = len(T)
    P = [0] * n
    C = R = 0

    for i in range(n):
        mirror = 2 * C - i
        if i < R:
            P[i] = min(R - i, P[mirror])
        
        a, b = i + P[i] + 1, i - P[i] - 1
        while a < n and b >= 0 and T[a] == T[b]:
            P[i] += 1
            a += 1
            b -= 1
        
        if i + P[i] > R:
            C, R = i, i + P[i]

    max_len, center_index = max((n, i) for i, n in enumerate(P))
    start = (center_index - max_len) // 2
    return s[start:start + max_len]
```

## Performance Comparison
| Approach                | Time Complexity | Best For |
|-------------------------|----------------|----------|
| Brute Force            | O(n^3)         | Small inputs |
| Expand Around Center   | O(n^2)         | General cases |
| Dynamic Programming    | O(n^2)         | Clear logic |
| Manacher’s Algorithm   | O(n)           | Large inputs |

## Conclusion
For interview purposes, **Expand Around Center** is simple and efficient. If you need the most optimized solution, use **Manacher’s Algorithm**.

---

**Author:** Muhammad Rezki Ananda

