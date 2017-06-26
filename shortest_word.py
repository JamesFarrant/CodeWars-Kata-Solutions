def find_short(s):
    s = s.split(' ')
    lens = []

    for i in s:
        lens.append(len(i))
    return min(lens)
