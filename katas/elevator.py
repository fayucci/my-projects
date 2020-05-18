def elevator(left, right, call):
    distance_right = abs(call-right)
    distance_left = abs(call-left)
    if distance_right == distance_left:
        return 'right'
    if left == call:
        return 'left'

print(elevator(0,0,0))
