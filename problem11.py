class Solution(object):
    def maxArea(self, height:list[int])->int:
        n = len(height)
        max = 0
        for i in range(n):
            for j in range(i+1,n):
                flag = (j-i)*(height[i] if height[i]<height[j] else height[j])
                if flag>max:
                    max = flag
        return max

    def maxArea2(self, height: list[int]) -> int:
        right = len(height) - 1
        left = 0
        max = 0
        while left<right:
            flag = (right - left) * (height[left] if height[left] < height[right] else height[right])
            if flag > max:
                max = flag
            if height[left]<=height[right] :
                left = left+1
            else:
                right = right - 1
        return  max

if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    i = Solution()
    print(i.maxArea(nums))
    print(i.maxArea2(nums))
"""
        :type height: List[int]
        :rtype: int
"""