class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        map = {}
        n  = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] = map[nums[i]]+1
                if map[nums[i]] > 2:
                    del nums[i]
        return len(nums)