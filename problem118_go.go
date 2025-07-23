func generate(numRows int) [][]int {
    // if numRows == 0 {
    //     return [][]int{}
    // }
    
    re_num := make([][]int, numRows)
    re_num[0] = []int{1}
    
    for i := 1; i < numRows; i++ {
        re_num[i] = make([]int, i+1)
        re_num[i][0] = 1
        re_num[i][i] = 1
        for j := 1; j < i; j++ {
            re_num[i][j] = re_num[i-1][j-1] + re_num[i-1][j]
        }
    }
    return re_num
}