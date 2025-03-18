class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(str)):
            while str[right] in char_set:
                char_set.remove(str[left])
                left += 1
            char_set.add(str[right])
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        return max_length
if __name__ == '__main__':
    s = "abcabcbb"
    i = Solution()
    print(i.lengthOfLongestSubstring(s))