def day_pass(lanternfish):
    for i in range(len(lanternfish)):
        if lanternfish[i] == 0:
            lanternfish.append(8)
        if lanternfish[i] < 7:
            lanternfish[i] = (lanternfish[i] - 1) % 7
        else:
            lanternfish[i] = lanternfish[i] - 1
    return lanternfish


def smart_day_pass(lanternfish_map):
    new_lanternfish_map = {}
    for i in range(6):
        new_lanternfish_map[i] = lanternfish_map[i + 1]
    new_lanternfish_map[6] = lanternfish_map[7] + lanternfish_map[0]
    new_lanternfish_map[7] = lanternfish_map[8]
    new_lanternfish_map[8] = lanternfish_map[0]
    return new_lanternfish_map


def fish_counter(lanternfish):
    counter = {i: 0 for i in range(9)}
    for fish in lanternfish:
        counter[fish] += 1
    return counter
