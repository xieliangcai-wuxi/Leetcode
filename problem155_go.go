package leetcode

import "math"

type MinStack struct {
	stack       []int
	min_element []int
}

func Constructor() MinStack {
	return MinStack{
		stack:       []int{},
		min_element: []int{math.MaxInt64},
	}
}

func (this *MinStack) Push(val int) {
	this.stack = append(this.stack, val)
	this.min_element = append(this.min_element, min(val, this.min_element[len(this.min_element)-1]))
}

func min(x int, y int) int {
	if x > y {
		return y
	} else {
		return x
	}
}

func (this *MinStack) Pop() {
	this.stack = this.stack[0 : len(this.stack)-1]
	this.min_element = this.min_element[0 : len(this.min_element)-1]

}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {

}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
