from day10 import knot_hash

key = 'jzgqcdpd'
hashes = [knot_hash(key + '-' + str(i)) for i in range(0, 128)]
bin_hashes = ["{:0128b}".format(int(s, 16)) for s in hashes]

print 'part 1:', sum([b.count('1') for b in bin_hashes])
