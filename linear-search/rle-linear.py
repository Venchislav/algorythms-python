def pack(s, cnt):
    if cnt > 1:
        return s + str(cnt)
    return s


def rle(s):
    last_symbol = s[0]
    res = []
    lastpos = 0
    for i in range(len(s)):
        if s[i] != last_symbol:
            res.append(pack(last_symbol, i - lastpos))
            lastpos = i
            last_symbol = s[i]
    res.append(last_symbol)
    return ''.join(res)


print(rle('AAABCDEEFFGIOP'))  # A3BCDE2F2GIOP
