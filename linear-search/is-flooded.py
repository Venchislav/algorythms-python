# kinda hard task

def is_flooded(h):
    max_pos = 0

    for i in range(len(h)):
        if h[i] > h[max_pos]:
            max_pos = i
    res = 0
    nowm = 0

    for i in range(max_pos):
        if h[i] > nowm:
            nowm = h[i]
        res += nowm - h[i]

    nowm = 0

    for i in range(len(h) - 1, max_pos, -1):
        if h[i] > nowm:
            nowm = h[i]
        res += nowm - h[i]
    return res
