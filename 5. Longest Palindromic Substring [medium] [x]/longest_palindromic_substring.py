class Solution(object):
    def longestPalindrome(self, s):
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

solution = Solution()
data = "babad"
result = solution.longestPalindrome(data)
print(result)