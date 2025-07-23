package main

func maxProfit(prices []int) int {
	prices_len := len(prices)
	var price_min int = prices[0]
	var profit_max int = 0
	for i := 0; i < prices_len; i++ {
		profit_max = max(profit_max, prices[i]-price_min)
		if price_min > prices[i] {
			price_min = prices[i]
		}
	}
	return profit_max
}
