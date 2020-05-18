def cube_checker(volume, side):
    if volume <= 0 or side <= 0: return False
    return volume == side**3