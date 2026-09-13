# Problem: Group Anagrams (#49)
# Difficulty: Medium
# Date: September 13, 2026
# Topic: Hashing
# Platform: LeetCode

class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
