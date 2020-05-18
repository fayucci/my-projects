def enough(cap, on, wait):
    remaining_seats = (cap - on)
    if cap >= (on + wait): return 0
    else: return print(wait - remaining_seats)

enough(100, 60, 50)