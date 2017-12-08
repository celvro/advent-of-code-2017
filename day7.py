#day7.py, this one's a garbage pile
from operator import itemgetter
import sys

def collect(l, index):
    return map(itemgetter(index), l)

# recursively get weight for each child, if unbalanced print out the expected weight and quit
def solve2(l, index):
    if len(l[index][2]) == 0:
        return l[index][1]
    else:
        ch = l[index][2]
        w = []
        for c in ch:
            w.append(solve2(l,c))
        if all(w[i] == w[i+1] for i in range(0, len(w)-1)):
            return l[index][1] + sum(w)
        else:
            for k,v in enumerate(w):
                if w.count(v) == 1:
                    print 'part 2:', l[l[index][2][k]][1] - (max(w)-min(w))
                    sys.exit(0)

lines = open('7.txt', 'r').readlines()
parents = [-1]*len(lines)

# each item in nodes is a list containing 3 elements, the name, weight, and a list of child indexes
nodes = []
# populate name and weights
for line in lines:
    parts = line.split()
    parts[1] = int(parts[1].replace('(','').replace(')',''))
    nodes.append([parts[0],parts[1],[]])

# populate parents and children
for line in lines:
    parts = line.split()
    if len(parts) > 2:
        for p in parts[3:]:
            p = p.replace(',', '')
            child_ind = collect(nodes,0).index(p)
            parent_ind = collect(nodes,0).index(parts[0])
            parents[child_ind] = parent_ind
            nodes[parent_ind][2].append(child_ind)

print 'part 1:', nodes[parents.index(-1)][0]
solve2(nodes, parents.index(-1))