package main

import (
	"day_16/tickets"
	"day_16/utils"
	"fmt"
	"strings"
)

func main() {
	input := utils.ReadFile("input.txt")
	rules, yourTicket, nearbyTickets := tickets.ParseInput(input)

	allTickets := append(nearbyTickets, yourTicket)
	validTickets, errorRate := tickets.ValidateTickets(rules, allTickets)

	// Part 1
	fmt.Printf("Error Rate: %d\n", errorRate)

	// Part 2
	possiblePositions := tickets.GetPossiblePositions(rules, validTickets)
	positions := tickets.GetPositions(possiblePositions)
	fmt.Printf("Label Positions: %+v\n", positions)
	result := 1
	for k, v := range positions {
		if strings.HasPrefix(k, "departure") {
			result = result * yourTicket[v]
		}
	}
	fmt.Printf("Result: %d\n", result)
}
