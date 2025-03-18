class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [1,]
        right = [0]*n
        right[-1] =1
        result = []
        for i in range(1,n):
            left.append(left[i-1]*nums[i-1])
        for i in reversed(range(n-1)):
            right[i] = right[i+1]*nums[i+1]
        print(left)
        print(right)
        for i in range(n):
            result.append(left[i]*right[i])
        return result
if __name__ == '__main__':
    nums = [1, 2, 0, 4]
    i = Solution()
    print(i.productExceptSelf(nums))