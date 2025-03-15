from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        re = 0
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum = sum + nums[j]
                if sum == k:
                    re =re + 1
        return re;

    def subarraySum2(self, nums: list[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # 初始条件，处理sum等于k的情况
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            # 查找当前前缀和减去k后的值是否存在于哈希表中
            count += prefix_counts.get(current_sum - k, 0)
            # 更新当前前缀和的出现次数
            prefix_counts[current_sum] += 1
        return count

if __name__ == '__main__':
    nums = [1, 1, 2]
    k = 2
    i = Solution()
    print(i.subarraySum2(nums,k))