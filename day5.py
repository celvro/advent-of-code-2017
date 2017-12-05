from timeit import default_timer as timer

f = open('5.txt', 'r')
jumps = map(int, f.readlines())
jumps2 = list(jumps)
end = len(jumps)

i = 0
count = 0
while i < end and i >= 0:
    next = i + jumps[i]
    jumps[i] += 1
    i = next
    count += 1
print 'part 1:', count

i = 0
count = 0
start = timer()
while i < end and i >= 0:
    next = i + jumps2[i]
    #jumps2[i] += ~(jumps2[i]-2) + 1 >> 31 | 1
    jumps2[i] += 1 if jumps2[i] < 3 else -1
    i = next
    count += 1
end = timer()
print 'part 2:', count, end - start