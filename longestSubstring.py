# Problem: Longest Substring Without Repeating Characters (#3)
# Difficulty: Medium
# Date: September 13, 2026
# Topic: Sliding Window, Hashing

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
