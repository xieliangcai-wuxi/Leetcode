class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        flag = nums.copy()
        for i in range(n):
            nums[(i+k)%n] = flag[i];
        """
        Do not return anything, modify nums in-place instead.
        """