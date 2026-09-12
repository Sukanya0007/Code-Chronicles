# Problem: Contains Duplicate (#217)
# Difficulty: Easy
# Date: September 12, 2026

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
