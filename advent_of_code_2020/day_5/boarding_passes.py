def get_seat_id(bp):
    bp = bp.replace("\n", "")
    row = int(bp[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(bp[-3:].replace("R", "1").replace("L", "0"), 2)
    return row * 8 + col


def find_my_seat(boarding_passes):
    seat_ids = [get_seat_id(bp) for bp in boarding_passes]
    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
            return i
