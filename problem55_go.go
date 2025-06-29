package main
import (
	"fmt"
)

// func contains(s []int, e int) bool {
//     for _, a := range s {
//         if a >= e {
//             return true
//         }
//     }
//     return false
// }

// func canJump(nums []int) bool {
//     maxcanjump := make([]int,len(nums))
//     maxcanjump[0] = nums[0]
//     for index,value := range nums{
//         if(contains(maxcanjump,index)){
//             maxcanjump_value := index + nums[index]
//             if(maxcanjump_value>len(nums)){
//                 return true
//             }else{
//                 maxcanjump[index] = maxcanjump_value
//             }
//         }else{
//             return false
//         }
//     }
//     return true
// }

func canJump(nums []int) bool {
    maxReachable := 0 
    for index,_ := range nums{
        if(index<=maxReachable){
            flag := index + nums[index]
            if(maxReachable < flag){
                maxReachable = flag
            }
            if(maxReachable > len(nums)-1){
                return true
            }
        }else{
            return false
        }
    }
    return true
}
func main() {
    nums := []int{2,3,1,1,4}
    fmt.Println(canJump(nums)) // 应该输出 true

    nums = []int{3,2,1,0,4}
    fmt.Println(canJump(nums)) // 应该输出 false

    nums = []int{0}
    fmt.Println(canJump(nums)) // 应该输出 true

    nums = []int{0,2,3}
    fmt.Println(canJump(nums)) // 应该输出 false
}