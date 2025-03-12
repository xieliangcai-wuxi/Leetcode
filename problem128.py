import collections


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

if __name__ == '__main__':
    nums = [100, 4, 4,200,  3, 2]
    i = Solution()
    print(i.longestConsecutive(nums))
"""
        :type nums: List[int]
        :rtype: int
"""