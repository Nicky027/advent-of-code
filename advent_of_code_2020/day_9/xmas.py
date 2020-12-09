def first_non_valid(numbers, preamble_size):
    for i in range(preamble_size, len(numbers) + 1):
        valid = False
        for number_1 in numbers[i - preamble_size : i]:
            for number_2 in numbers[i - preamble_size : i]:
                if number_1 != number_2 and number_1 + number_2 == numbers[i]:
                    valid = True
                    break
            if valid:
                break
        if valid:
            continue
        else:
            return numbers[i]

    return 0


def consecutive_add_up(number, numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == number:
            break

        consecutive_numbers = [numbers[i]]
        for j in range(i + 1, len(numbers)):
            consecutive_numbers.append(numbers[j])
            if sum(consecutive_numbers) == number:
                return consecutive_numbers
            elif sum(consecutive_numbers) > number:
                break

    return []
