class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        n = len(intervals)
        for i in range(1,n):
            if result[-1][1]>=intervals[i][0] :
                if result[-1][1]<=intervals[i][1] :
                    result[-1] = [result[-1][0],intervals[i][1]]
                else:
                    continue
            else :
                result.append(intervals[i])
        return result

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    i = Solution()
    print(i.merge(intervals))