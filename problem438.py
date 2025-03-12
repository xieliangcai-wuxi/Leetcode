from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 初始化结果列表和长度检查
        re_list = []
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return re_list

        # 初始化频率字典
        p_count = defaultdict(int)
        window = defaultdict(int)
        for char in p:
            p_count[char] += 1

        # 初始化第一个窗口
        for i in range(p_len):
            window[s[i]] += 1

        # 检查第一个窗口是否符合条件
        if window == p_count:
            re_list.append(0)

        # 滑动窗口过程
        for i in range(1, s_len - p_len + 1):
            # 移除左边界字符
            left_char = s[i - 1]
            if window[left_char] == 1:
                del window[left_char]
            else:
                window[left_char] -= 1

            # 添加右边界字符
            right_char = i + p_len - 1
            window[s[right_char]] += 1

            # 比较当前窗口是否符合条件
            if window == p_count:
                re_list.append(i)

        return re_list

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    i = Solution()
    print(i.findAnagrams(s,p))