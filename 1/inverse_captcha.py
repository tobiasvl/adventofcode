from itertools import tee, islice, chain, izip, cycle

with open('input.txt') as f:
    number_string = [int(x) for x in f.readline().strip()]


def inverse_captcha1():
    def previous_and_next(some_iterable):
        prevs, items, nexts = tee(some_iterable, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])
        return izip(prevs, items, nexts)

    acc = 0
    for previous, item, nxt in previous_and_next(number_string):
        if nxt is None:
            nxt = number_string[0]
        if item == nxt:
            acc = acc + item
    return acc


def inverse_captcha2():
    acc = 0
    halfway = len(number_string) / 2

    for idx, item in enumerate(number_string):
        circular_list = cycle(number_string)
        for i in range(idx):
            next(circular_list)
        a = -1
        for nxt in circular_list:
            a = a + 1
            if a == halfway:
                break
        if item == nxt:
            acc = acc + item
    return acc


print "Captcha 1: %s" % inverse_captcha1()
print "Captcha 2: %s" % inverse_captcha2()
