#day8.py
from collections import defaultdict

reg = defaultdict(int)
highest = 0

for line in open('8.txt', 'r').readlines():
    p = line.split()
    
    p[2] = -int(p[2]) if p[1]=='dec' else int(p[2])
    if eval(str(reg[p[4]]) + p[5] + p[6]):
       reg[p[0]] += p[2]
       if reg[p[0]] > highest: highest = reg[p[0]]

print 'part 1:', max(reg.values())
print 'part 2:', highest