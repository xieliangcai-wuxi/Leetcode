// func coinChange(coins []int, amount int) int {
// 	coins_len := len(coins)
//     dp := make([]int,amount+1)
// 	dp[0] = 0
// 	for i:= 1;i < amount+1;i++ {
// 		for j := 0;j < coins_len;j++ {
// 			flag := i-coins[j]
// 			first_calculation := 0
// 			count := 0
// 			if(flag>=0){
// 				if(first_calculation == 0){
// 					dp[i] = dp[flag] + 1
// 					first_calculation++
// 				}else{
// 					if(dp[flag] + 1 < dp[i]){
// 						dp[i] = dp[flag] + 1
// 					}
// 				}
// 			}else{
// 				count++
// 			}
// 			if(count == coins_len){
// 				dp[i] = -1
// 			}
// 		}
// 	}
// 	return dp[account]

// }

func coinChange(coins []int, amount int) int {
	coins_len := len(coins)
    dp := make([]int,amount+1)
	dp[0] = 0
	for i := 1;i < amount+1 ; i++ {
		dp[i] = amount + 1
	}
	for i := 1;i < amount+1;i++ {
		for j := 0;j < coins_len;j++ {
			flag := i-coins[j]
			if( flag >= 0 && dp[flag] + 1 < dp[i]){
				dp[i] = dp[flag] + 1
			}
		}
	}
	if(dp[amount] >= amount + 1){
		dp[amount] = -1
	}
	return dp[amount]
}

// 下面的代码是ai进一步精简过后的
func coinChange(coins []int, amount int) int {
    dp := make([]int, amount+1)
    for i := 1; i <= amount; i++ {
        dp[i] = amount + 1
    }
    
    for i := 1; i <= amount; i++ {
        for _, coin := range coins {
            if coin <= i && dp[i-coin]+1 < dp[i] {
                dp[i] = dp[i-coin] + 1
            }
        }
    }
    
    if dp[amount] > amount {
        return -1
    }
    return dp[amount]
}