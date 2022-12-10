def get_registry_values(inputs: list) -> dict:
    cycle = 1
    registry_values = {cycle: 1}

    for input in inputs:
        parsed_input = input.replace("\n", "").split(" ")
        instruction = parsed_input[0]

        if instruction == "noop":
            cycle += 1
            registry_values[cycle] = registry_values[cycle - 1]
        else:
            value = int(parsed_input[1])
            cycle += 2
            registry_values[cycle - 1] = registry_values[cycle - 2]
            registry_values[cycle] = registry_values[cycle - 1] + value

    return registry_values


def get_signal_strengths(registry_values: dict, cycles: int) -> list:
    strengths = []
    for cycle in cycles:
        strengths.append(cycle * registry_values[cycle])
    return strengths


def crt_render(registry_values: dict):
    screen = [["." for _ in range(40)] for _ in range(6)]
    for cycle, value in registry_values.items():
        row = int((cycle - 1) / 40)
        column = (cycle - 1) % 40
        print(value, column)
        if abs(value - column) <= 1:
            screen[row][column] = "#"

    for row in screen:
        print("".join(row))
