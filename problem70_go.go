// func climbStairs(n int) int {
//     dp :=make([]int,n)
// 	dp[0] = 1
//     if(n > 1){
//         dp[1] = 2
//     } 
//     if(n > 2){
//         for i := 2;i < n; i++ {
// 		    dp[i] = dp[i-1] + dp[i-2]
// 	    }
//     } 
// 	return dp[n-1]
// }
func climbStairs(n int) int {
    dp :=make([]int,n+1)
    dp[0] = 1
	dp[1] = 1
	for i := 2;i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	} 
	return dp[n]
}