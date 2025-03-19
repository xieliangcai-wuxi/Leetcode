import collections
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

