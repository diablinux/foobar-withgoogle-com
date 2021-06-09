def solution(x, y):
    set_difference = list(set(x) ^ set(y))
    return set_difference[0]
