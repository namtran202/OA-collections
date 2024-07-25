def countSubstrings(s: str) -> int:
    count = 0
    for index in range(len(s)):
        left, right = index, index
        while left > -1 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        left, right = index, index + 1
        while left > -1 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count


def count_non_overlapping_palindromic_substrings(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    # Step 1: Identify all palindromic substrings using dynamic programming
    dp = [[False] * n for _ in range(n)]
    palindromes = []

    # Single character substrings
    for i in range(n):
        dp[i][i] = True
        palindromes.append((i, i))

    # Two character substrings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            palindromes.append((i, i + 1))

    # Substrings longer than two characters
    for length in range(3, n + 1):  # length is the length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                palindromes.append((i, j))

    # Step 2: Select the maximum number of non-overlapping palindromic substrings
    palindromes.sort(key=lambda x: x[1])  # Sort by end index

    count = 0
    end = -1  # Initialize end to -1 to allow the first palindrome to be selected

    for start, finish in palindromes:
        if start > end:
            count += 1
            end = finish

    return count


# Example usage:
s1 = "abc"
print(count_non_overlapping_palindromic_substrings(s1))  # Output: 3

s2 = "aababaabce"
print(count_non_overlapping_palindromic_substrings(s2))  # Output: 3
