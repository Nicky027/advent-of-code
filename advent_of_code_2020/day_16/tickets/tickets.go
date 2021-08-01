package tickets

import (
	"log"
	"sort"
	"strconv"
	"strings"
)

type Rule struct {
	Label  string
	Ranges []Range
}

// Range holds min and max values for a rule
type Range struct {
	Min int
	Max int
}

// Ticket is a list of numbers
type Ticket []int

// Parse input takes a raw input array of strings corresponding to lines and returns rules, your ticket, and nearby tickets
func ParseInput(input []string) ([]Rule, Ticket, []Ticket) {
	rules := make([]Rule, 0)
	yourTicket := make(Ticket, 0)
	nearbyTickets := make([]Ticket, 0)

	section := "rules"

	for _, line := range input {
		switch line {
		case "":
			continue
		case "your ticket:":
			section = "your ticket"
			continue
		case "nearby tickets:":
			section = "nearby tickets"
			continue
		}

		switch section {
		case "rules":
			label, ranges := parseRule(line)
			rules = append(rules, Rule{label, ranges})
		case "your ticket":
			yourTicket = parseTicket(line)
		case "nearby tickets":
			nearbyTicket := parseTicket(line)
			nearbyTickets = append(nearbyTickets, nearbyTicket)
		}
	}

	return rules, yourTicket, nearbyTickets
}

func parseRule(line string) (string, []Range) {
	lineParts := strings.Split(line, ":")
	label := lineParts[0]
	rawRanges := strings.Split(strings.TrimSpace(lineParts[1]), "or")
	ranges := make([]Range, 0)

	for _, r := range rawRanges {
		minMax := strings.Split(strings.TrimSpace(r), "-")
		min, err := strconv.Atoi(minMax[0])
		if err != nil {
			log.Fatal(err)
		}
		max, err := strconv.Atoi(minMax[1])
		if err != nil {
			log.Fatal(err)
		}
		ranges = append(ranges, Range{min, max})
	}

	return label, ranges
}

func parseTicket(line string) Ticket {
	ticket := make(Ticket, 0)
	lineParts := strings.Split(line, ",")
	for _, part := range lineParts {
		number, err := strconv.Atoi(part)
		if err != nil {
			log.Fatal(err)
		}
		ticket = append(ticket, number)
	}
	return ticket
}

func ValidateTickets(rules []Rule, tickets []Ticket) ([]Ticket, int) {
	validTickets := make([]Ticket, 0)
	var errorRate int

	for _, ticket := range tickets {
		valid := true
	ticketLoop:
		for _, number := range ticket {
			for _, rule := range rules {
				for _, ruleRange := range rule.Ranges {
					if number >= ruleRange.Min && number <= ruleRange.Max {
						continue ticketLoop
					}
				}
			}
			valid = false
			errorRate += number
		}
		if valid {
			validTickets = append(validTickets, ticket)
		}
	}

	return validTickets, errorRate
}

func GetPossiblePositions(rules []Rule, tickets []Ticket) map[string][]int {
	possiblePositions := make(map[string][][]int)
	possiblePositionsIntersection := make(map[string][]int)

	for _, ticket := range tickets {
		possiblePositionsByTicket := getPossiblePositionsByTicket(rules, ticket)
		for k, v := range possiblePositionsByTicket {
			possiblePositions[k] = append(possiblePositions[k], v)
		}
	}

	for k, v := range possiblePositions {
		possiblePositionsIntersection[k] = getArrayIntersection(v)
	}

	return possiblePositionsIntersection
}

func getPossiblePositionsByTicket(rules []Rule, ticket Ticket) map[string][]int {
	possiblePositions := make(map[string][]int)

	for _, rule := range rules {
	ticketLoop:
		for i, number := range ticket {
			for _, ruleRange := range rule.Ranges {
				if number >= ruleRange.Min && number <= ruleRange.Max {
					possiblePositions[rule.Label] = append(possiblePositions[rule.Label], i)
					continue ticketLoop
				}
			}
		}
	}

	return possiblePositions
}

func getArrayIntersection(arrays [][]int) []int {
	length := len(arrays)
	intersection := make([]int, 0)
	elementCount := make(map[int]int)

	for _, array := range arrays {
		for _, element := range array {
			count, ok := elementCount[element]
			if ok {
				elementCount[element] = count + 1
			} else {
				elementCount[element] = 1
			}
		}
	}

	for k, v := range elementCount {
		if v == length {
			intersection = append(intersection, k)
		}
	}

	return intersection
}

func GetPositions(possiblePositions map[string][]int) map[string]int {
	positions := make(map[string]int)
	takenPositions := make([]int, 0)

	countsOfPossiblePositions := make([]struct {
		Label string
		Count int
	}, 0)

	for k, v := range possiblePositions {
		countsOfPossiblePositions = append(countsOfPossiblePositions, struct {
			Label string
			Count int
		}{k, len(v)})
	}

	sort.Slice(countsOfPossiblePositions, func(i, j int) bool {
		return countsOfPossiblePositions[i].Count < countsOfPossiblePositions[j].Count
	})

	for _, v := range countsOfPossiblePositions {
	labelLoop:
		for _, position := range possiblePositions[v.Label] {
			if !contains(takenPositions, position) {
				takenPositions = append(takenPositions, position)
				positions[v.Label] = position
				break labelLoop
			}
		}
	}

	return positions
}

func contains(array []int, a int) bool {
	for _, v := range array {
		if a == v {
			return true
		}
	}
	return false
}
