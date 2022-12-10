def get_visited_tail_positions(inputs: list) -> dict:
    h_position = (0, 0)
    t_position = (0, 0)
    t_visited_positions = {str(t_position): 1}

    for input in inputs:
        parsed_input = input.replace("\n", "").split(" ")
        direction = parsed_input[0]
        steps = int(parsed_input[1])

        for _ in range(steps):
            if direction == "R":
                h_position = (h_position[0] + 1, h_position[1])
            elif direction == "L":
                h_position = (h_position[0] - 1, h_position[1])
            elif direction == "U":
                h_position = (h_position[0], h_position[1] + 1)
            elif direction == "D":
                h_position = (h_position[0], h_position[1] - 1)

            x_distance = h_position[0] - t_position[0]
            y_distance = h_position[1] - t_position[1]

            if x_distance > 1 and y_distance == 0:
                t_position = (t_position[0] + 1, t_position[1])

            if x_distance < -1 and y_distance == 0:
                t_position = (t_position[0] - 1, t_position[1])

            if y_distance > 1 and x_distance == 0:
                t_position = (t_position[0], t_position[1] + 1)

            if y_distance < -1 and x_distance == 0:
                t_position = (t_position[0], t_position[1] - 1)

            if x_distance == 1 and y_distance > 1:
                t_position = (t_position[0] + 1, t_position[1] + 1)

            if x_distance == 1 and y_distance < -1:
                t_position = (t_position[0] + 1, t_position[1] - 1)

            if x_distance == -1 and y_distance > 1:
                t_position = (t_position[0] - 1, t_position[1] + 1)

            if x_distance == -1 and y_distance < -1:
                t_position = (t_position[0] - 1, t_position[1] - 1)

            if y_distance == 1 and x_distance > 1:
                t_position = (t_position[0] + 1, t_position[1] + 1)

            if y_distance == 1 and x_distance < -1:
                t_position = (t_position[0] - 1, t_position[1] + 1)

            if y_distance == -1 and x_distance > 1:
                t_position = (t_position[0] + 1, t_position[1] - 1)

            if y_distance == -1 and x_distance < -1:
                t_position = (t_position[0] - 1, t_position[1] - 1)

            t_position_key = str(t_position)
            if not t_visited_positions.get(t_position_key):
                t_visited_positions[t_position_key] = 1
            else:
                t_visited_positions[t_position_key] += 1

    return t_visited_positions


def get_visited_tail_positions_2(inputs: list, knots: int = 10) -> dict:
    positions = [(0, 0) for _ in range(knots)]
    t_visited_positions = {str(positions[-1]): 1}

    for input in inputs:
        parsed_input = input.replace("\n", "").split(" ")
        direction = parsed_input[0]
        steps = int(parsed_input[1])

        for _ in range(steps):
            if direction == "R":
                positions[0] = (positions[0][0] + 1, positions[0][1])
            elif direction == "L":
                positions[0] = (positions[0][0] - 1, positions[0][1])
            elif direction == "U":
                positions[0] = (positions[0][0], positions[0][1] + 1)
            elif direction == "D":
                positions[0] = (positions[0][0], positions[0][1] - 1)

            for i in range(knots - 1):
                x_distance = positions[i][0] - positions[i + 1][0]
                y_distance = positions[i][1] - positions[i + 1][1]

                if x_distance > 1 and y_distance == 0:
                    positions[i + 1] = (
                        positions[i + 1][0] + 1,
                        positions[i + 1][1],
                    )

                elif x_distance < -1 and y_distance == 0:
                    positions[i + 1] = (
                        positions[i + 1][0] - 1,
                        positions[i + 1][1],
                    )

                elif y_distance > 1 and x_distance == 0:
                    positions[i + 1] = (
                        positions[i + 1][0],
                        positions[i + 1][1] + 1,
                    )

                elif y_distance < -1 and x_distance == 0:
                    positions[i + 1] = (
                        positions[i + 1][0],
                        positions[i + 1][1] - 1,
                    )

                elif x_distance >= 1 and y_distance > 1:
                    positions[i + 1] = (
                        positions[i + 1][0] + 1,
                        positions[i + 1][1] + 1,
                    )

                elif x_distance >= 1 and y_distance < -1:
                    positions[i + 1] = (
                        positions[i + 1][0] + 1,
                        positions[i + 1][1] - 1,
                    )

                elif x_distance <= -1 and y_distance > 1:
                    positions[i + 1] = (
                        positions[i + 1][0] - 1,
                        positions[i + 1][1] + 1,
                    )

                elif x_distance <= -1 and y_distance < -1:
                    positions[i + 1] = (
                        positions[i + 1][0] - 1,
                        positions[i + 1][1] - 1,
                    )

                elif y_distance >= 1 and x_distance > 1:
                    positions[i + 1] = (
                        positions[i + 1][0] + 1,
                        positions[i + 1][1] + 1,
                    )

                elif y_distance >= 1 and x_distance < -1:
                    positions[i + 1] = (
                        positions[i + 1][0] - 1,
                        positions[i + 1][1] + 1,
                    )

                elif y_distance <= -1 and x_distance > 1:
                    positions[i + 1] = (
                        positions[i + 1][0] + 1,
                        positions[i + 1][1] - 1,
                    )

                elif y_distance <= -1 and x_distance < -1:
                    positions[i + 1] = (
                        positions[i + 1][0] - 1,
                        positions[i + 1][1] - 1,
                    )

            # print(positions[5], positions[6])

            t_position_key = str(positions[-1])
            if not t_visited_positions.get(t_position_key):
                t_visited_positions[t_position_key] = 1
            else:
                t_visited_positions[t_position_key] += 1

    return t_visited_positions
