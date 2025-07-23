package leetcode

//暴力解法
// func dailyTemperatures(temperatures []int) []int {
// 	return_int := []int{}
// 	tem_len := len(temperatures)
// 	for i := 0; i < tem_len; i++ {
// 		for j := i + 1; j < tem_len; j++ {
// 			if temperatures[i] < temperatures[j] {
// 				return_int = append(return_int, j-i)
// 				break
// 			}
// 			if j == tem_len-1 {
// 				return_int = append(return_int, 0)
// 			}
// 		}
// 	}
// 	return_int = append(return_int, 0)
// 	return return_int
// }
//运用栈的解法
func dailyTemperatures(temperatures []int) []int {
	length := len(temperatures)
	ans := make([]int, length)
	stack := []int{}
	for i := 0; i < length; i++ {
		temperature := temperatures[i]
		for len(stack) > 0 && temperature > temperatures[stack[len(stack)-1]] {
			prevIndex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[prevIndex] = i - prevIndex
		}
		stack = append(stack, i)
	}
	return ans
}
