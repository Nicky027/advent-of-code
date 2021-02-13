package numbers

// GetSpokenNumber gives the numbers that was spoken at turn n given the startingNumbers
func GetSpokenNumber(startingNumbers []int, n int) int {
	if n <= 0 {
		return 0
	}

	if n < len(startingNumbers) {
		return startingNumbers[n-1]
	}

	var lastSpokenNumber int
	spokenNumbers := make(map[int][]int)

	for i, number := range startingNumbers {
		spokenNumbers[number] = append(spokenNumbers[number], i)
		lastSpokenNumber = number
	}

	for i := len(startingNumbers); i < n; i++ {
		lastSpokenNumberHistory, ok := spokenNumbers[lastSpokenNumber]
		if !ok || len(lastSpokenNumberHistory) == 1 {
			lastSpokenNumber = 0
		} else {
			previousLastSpokenTurn := lastSpokenNumberHistory[len(lastSpokenNumberHistory)-2]
			lastSpokenTurn := lastSpokenNumberHistory[len(lastSpokenNumberHistory)-1]
			difference := lastSpokenTurn - previousLastSpokenTurn
			lastSpokenNumber = difference
		}
		spokenNumbers[lastSpokenNumber] = append(spokenNumbers[lastSpokenNumber], i)
	}

	return lastSpokenNumber
}
