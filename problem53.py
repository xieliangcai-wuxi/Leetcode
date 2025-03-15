class Solution:
    # 时间复杂度太高了
    # def maxSubArray(self, nums: list[int]) -> int:
    #     n = len(nums)
    #     max=0
    #     for i in range(n):
    #         sum = 0
    #         for j in range(i,n):
    #             print(j)
    #             sum =sum+nums[j]
    #             if sum>max :
    #                 max = sum
    #     return max

    def maxSubArray(self, nums: list[int]) -> int:
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global
if __name__ == '__main__':
    n1 = [-2,1,-3,4,-1,2,1,-5,4]
    i = Solution()
    print(i.maxSubArray(n1))