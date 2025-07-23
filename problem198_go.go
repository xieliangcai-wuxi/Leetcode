func rob(nums []int) int {
	nums_len := len(nums)
    dp := make([]int,nums_len)
	dp[0] = nums[0]
    if nums_len == 1{
        return dp[0]
    }
	if(nums[0]>nums[1]){
		dp[1] = nums[0]	
	}else{
		dp[1] = nums[1]
	}	
	for i := 2;i < nums_len;i++{
		dp[i] = max(dp[i-2]+nums[i],dp[i-1])
	}
	return dp[nums_len-1]
}