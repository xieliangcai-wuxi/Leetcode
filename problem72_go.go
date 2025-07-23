func min(a int,b int,c int) int{
	if(c<=b && c<=a){
		return c
	}
	if(b<=a && b<=c){
		return b
	}else{
		return a
	}
}
func minDistance(word1 string, word2 string) int {
	m,n := len(word1)+1,len(word2)+1
    dp := make([][]int,m)
	for i := 0;i < m;i++ {
		dp[i] = make([]int,n)
		dp[i][0] = i
	}
	for j := 0; j < n ;j++ {
		dp[0][j] = j
	}
	for i := 1;i < m;i++ {
		for j := 1; j < n ;j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			}else{
				dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
			}
		}
	}
	return dp[m-1][n-1]
}
