def high_and_low(numbers):
    res = []
    for i in numbers.split():
        res.append(int(i))
    return  str(max(res)) + ' ' + str(min(res))
