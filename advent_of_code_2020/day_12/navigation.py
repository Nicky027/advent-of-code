import numpy as np


class Ferry:
    def __init__(self):
        self.angle = 90
        self.position = (0, 0)
        self.waypoint = (10, 1)

    def turn(self, direction, angle):
        if direction == "R":
            self.angle = (self.angle + angle) % 360
        else:
            self.angle = (self.angle - angle) % 360

    def rotate_waypoint(self, direction, angle):
        if direction == "R":
            rotate_90 = np.array([[0, 1], [-1, 0]])
        elif direction == "L":
            rotate_90 = np.array([[0, -1], [1, 0]])
        new_waypoint = np.linalg.matrix_power(rotate_90, int(angle / 90)).dot(
            np.array(self.waypoint)
        )
        self.waypoint = tuple(new_waypoint)

    def get_direction(self):
        if self.angle == 90:
            return "E"
        elif self.angle == 180:
            return "S"
        elif self.angle == 270:
            return "W"
        elif self.angle == 0:
            return "N"

    def traverse(self, route):
        for x in route:
            direction = x[0]
            steps = int(x[1:])

            if direction in ["R", "L"]:
                self.turn(direction, steps)
                continue

            if direction == "F":
                direction = self.get_direction()

            if direction == "E":
                for _ in range(steps):
                    self.position = (self.position[0] + 1, self.position[1])

            elif direction == "W":
                for _ in range(steps):
                    self.position = (self.position[0] - 1, self.position[1])

            elif direction == "N":
                for _ in range(steps):
                    self.position = (self.position[0], self.position[1] + 1)

            elif direction == "S":
                for _ in range(steps):
                    self.position = (self.position[0], self.position[1] - 1)

            else:
                raise SystemExit("Cannot interpret direction. Exiting.")

    def distance(self):
        return abs(self.position[0]) + abs(self.position[1])

    def traverse_v2(self, route):
        for x in route:
            direction = x[0]
            steps = int(x[1:])

            if direction in ["R", "L"]:
                self.rotate_waypoint(direction, steps)
                continue

            if direction == "F":
                new_position = np.array(self.position) + steps * np.array(
                    self.waypoint
                )
                self.position = tuple(new_position)

            elif direction == "E":
                for _ in range(steps):
                    self.waypoint = (self.waypoint[0] + 1, self.waypoint[1])

            elif direction == "W":
                for _ in range(steps):
                    self.waypoint = (self.waypoint[0] - 1, self.waypoint[1])

            elif direction == "N":
                for _ in range(steps):
                    self.waypoint = (self.waypoint[0], self.waypoint[1] + 1)

            elif direction == "S":
                for _ in range(steps):
                    self.waypoint = (self.waypoint[0], self.waypoint[1] - 1)

            else:
                raise SystemExit("Cannot interpret direction. Exiting.")
