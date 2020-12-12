from navigation import Ferry


def main():
    with open("input.txt", "r") as file:
        directions = file.readlines()

    route = [x.replace("\n", "") for x in directions]

    ferry = Ferry()
    ferry.traverse(route)
    print(ferry.distance())

    ferry2 = Ferry()
    ferry2.traverse_v2(route)
    print(ferry2.distance())


if __name__ == "__main__":
    main()
