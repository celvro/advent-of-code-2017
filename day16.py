import string
from timeit import default_timer as timer


def s(x, arr):
    return arr[-x:] + arr[:-x]


def x(a, b, arr):
    tmp_array = list(arr)
    tmp_array[a] = arr[b]
    tmp_array[b] = arr[a]
    return ''.join(tmp_array)


def p(a, b, arr):
    ind_a = arr.find(a)
    ind_b = arr.find(b)
    return x(ind_a, ind_b, arr)


def dance(order, moves, checked):
    if order in checked:
        return checked[order]
    tmp = order
    for d in moves:
        move = d[0]
        if move == 's':
            tmp = s(int(d[1:]), tmp)
        elif move == 'x':
            a, b = map(int, d[1:].split('/'))
            tmp = x(a, b, tmp)
        elif move == 'p':
            a, b = d[1:].split('/')
            tmp = p(a, b, tmp)
    checked[order] = tmp
    return tmp


def main():
    moves = open('16.txt', 'r').read().split(',')
    prog = string.ascii_lowercase[:16]
    seen = {}
    prog = dance(prog, moves, seen)
    print 'part 1:', prog

    # better use pypy or this takes forever, might refactor to store sequences till they repeat and
    # then print out which one would fall on the 1 billionth loop
    for _ in xrange(1000000000 - 1):
        prog = dance(prog, moves, seen)
    print 'part 2:', prog


if __name__ == '__main__':
    start_tm = timer()
    main()
    print 'time:', timer() - start_tm
