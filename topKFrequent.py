# Problem: Top K Frequent Elements (#347)
# Difficulty: Medium
# Date: September 13, 2026
# Topic: Hashing

class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key=count.get, reverse=True)[:k]
