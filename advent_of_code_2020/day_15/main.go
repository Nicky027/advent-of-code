package main

import (
	"day_15/numbers"
	"fmt"
)

func main() {
	puzzleInput := []int{0, 14, 6, 20, 1, 4}
	fmt.Println(numbers.GetSpokenNumber(puzzleInput, 2020))
	fmt.Println(numbers.GetSpokenNumber(puzzleInput, 30000000))
}
