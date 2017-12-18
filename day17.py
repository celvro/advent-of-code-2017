from timeit import default_timer as timer


def main():
    steps = 367
    pos = 0
    values = [0]
    for i in range(1, 2018):
        pos = (pos + steps) % i + 1
        values.insert(pos, i)
    # probably fails if 2017 is the last number in list
    print 'part 1:', values[values.index(2017) + 1]

    ans = 0
    pos = 0
    for i in xrange(1, 50000001):
        pos = (pos + steps) % i + 1
        # 0 will always be at index 0 so just check if something should be inserted at index 1,
        # actual insert too slow to run 50 million times
        if pos == 1:
            ans = i
    print 'part 2:', ans


if __name__ == '__main__':
    start_tm = timer()
    main()
    print 'time:', timer() - start_tm
