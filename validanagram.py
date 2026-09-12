# Problem: Valid Anagram (#242)
# Difficulty: Easy
# Date: September 12, 2026

class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
