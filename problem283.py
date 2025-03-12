class Solution(object):
    # 用循环的方式
    def moveZeroes(self, nums:list[int]):
        flag = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[flag] = nums[index]
                flag = flag+1
        for index in range(flag, len(nums)):
            nums[index] = 0
    #用双指针的方式
    def moveZeroes2(self, nums:list[int]):
        left = 0
        right = 0
        while right<len(nums):
            if nums[right] !=0 :
                flag = nums[left]
                nums[left] = nums[right]
                nums[right] = flag
                left = left + 1
            right += 1

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    i = Solution()
    i.moveZeroes(nums)
    print(nums)
    nums2 = [0, 1, 0, 3, 12]
    i.moveZeroes2(nums2)
    print(nums2)
"""
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
"""