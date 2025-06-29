func merge(intervals [][]int) [][]int {
    if len(intervals) == 0 {
        return nil
    }
    
    // 首先按照区间起始位置排序（重要！）
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    
    outcome := [][]int{intervals[0]} // 直接初始化包含第一个区间
    
    for i := 1; i < len(intervals); i++ {
        last := outcome[len(outcome)-1]
        // 当前区间与最后一个区间有重叠
        if intervals[i][0] <= last[1] {
            // 更新结束时间（取较大值）
            if intervals[i][1] > last[1] {
                outcome[len(outcome)-1][1] = intervals[i][1]
            }
        } else {
            // 无重叠时添加新区间
            outcome = append(outcome, intervals[i])
        }
    }
    return outcome
}