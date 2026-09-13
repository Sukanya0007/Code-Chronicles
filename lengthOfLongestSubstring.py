# Problem: Longest Substring Without Repeating Characters (#3)
# Difficulty: Medium
# Pattern: Sliding Window
# Date: September 13, 2026

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
