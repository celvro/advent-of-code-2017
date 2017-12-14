def _hash(lengths, arr, pos, skip):
    for length in lengths:
        end = (length + pos - 1) % len(arr)
        if end < pos:
            tmp = arr[pos:] + arr[:end + 1]
        else:
            tmp = arr[pos:end + 1]
        tmp = tmp[::-1]
        for i in xrange(0, length):
            j = (pos + i) % len(arr)
            arr[j] = tmp[i]
        pos = (pos + length + skip) % len(arr)
        skip += 1
    return arr, pos, skip


def knot_hash(s):
    tmp = range(0, 256)
    p, skip_s = 0, 0
    len_arr = map(ord, s) + [17, 31, 73, 47, 23]
    for i in xrange(0, 64):
        tmp, p, skip_s = _hash(len_arr, tmp, p, skip_s)
    result = []
    # get tuples in groups of 16
    for x in zip(*[iter(tmp)] * 16):
        # reduce gives the decimal result of xor, for string conversion consult
        # https://docs.python.org/2.4/lib/typesseq-strings.html
        result.append('%02x' % reduce(lambda a, b: a ^ b, x, 0))
    return ''.join(result)


def main():
    original_inp = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'
    arr1, _, _ = _hash(map(int, original_inp.split(',')), range(0, 256), 0, 0)
    print 'part 1:', arr1[0] * arr1[1]
    print 'part 2:', knot_hash(original_inp)


if __name__ == "__main__":
    main()
