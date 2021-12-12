from collections import Counter


def parse_inputs(inputs):
    caves = {}
    for input in inputs:
        connection_caves = input.split("-")
        for i, cave in enumerate(connection_caves):
            if caves.get(cave):
                caves[cave].add(connection_caves[abs(1 - i)])
            else:
                caves[cave] = {connection_caves[abs(1 - i)]}
    return caves


def find_paths(caves, paths, part=1):
    new_paths = []
    for i, path in enumerate(paths):
        if should_stop_path(path, part):
            continue
        next_possible_caves = caves[path[-1]]
        for cave in next_possible_caves:
            new_path = path.copy()
            new_path.append(cave)
            new_paths.append(new_path)
        del paths[i]
    paths.extend(new_paths)
    return paths


def clean_paths(paths, part=1):
    if part == 1:
        return [path for path in paths if path[-1] == "end"]
    elif part == 2:
        cleaned_paths = []
        for path in paths:
            lower_cave_occurences = Counter(
                [
                    cave
                    for cave in path
                    if cave == cave.lower() and cave not in ["start", "end"]
                ]
            )
            if (
                sum(
                    [
                        1
                        for occurences in lower_cave_occurences.values()
                        if occurences == 2
                    ]
                )
                <= 1
                and path[-1] == "end"
            ):
                cleaned_paths.append(path)
        return cleaned_paths


def should_stop_path(path, part=1):
    last_cave = path[-1]
    if part == 1:
        return last_cave == "end" or (
            last_cave in path[0:-1] and last_cave == last_cave.lower()
        )
    elif part == 2:
        if last_cave != last_cave.lower():
            return False

        if last_cave == "end" or (last_cave == "start" and len(path) > 1):
            return True

        lower_cave_occurences = Counter(
            [
                cave
                for cave in path
                if cave == cave.lower() and cave not in ["start", "end"]
            ]
        )

        occured_twice = 0
        for occurences in lower_cave_occurences.values():
            if occurences > 2:
                return True
            if occurences == 2:
                occured_twice += 1

        return occured_twice > 1
