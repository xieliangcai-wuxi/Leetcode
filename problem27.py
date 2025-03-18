class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):  # 从后向前遍历
            if nums[i] == val:
                del nums[i]                   # 直接删除元素
        return len(nums)
    # 双指针
    def removeElement2(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:  # 保留非目标值
                nums[slow] = nums[fast]
                slow += 1
        return slow  # 新数组长度为 slow
