def generator(num, const, mod):
    while True:
        num = num * const % 2147483647
        if num % mod == 0:
            yield num & 0xFFFF


factor_a, factor_b = 16807, 48271
a, b = 277, 349
gen_a = generator(a, factor_a, 1)
gen_b = generator(b, factor_b, 1)
print 'part 1:', sum(next(gen_a) == next(gen_b) for _ in xrange(40000000))

gen_a = generator(a, factor_a, 4)
gen_b = generator(b, factor_b, 8)
print 'part 2:', sum(next(gen_a) == next(gen_b) for _ in xrange(5000000))
