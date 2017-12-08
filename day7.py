#day7.py, this one's a garbage pile
from operator import itemgetter
import sys

def collect(l, index):
    return map(itemgetter(index), l)

def get_total_weight(l, index):
    if len(l[index][2]) == 0:
        return l[index][1]
    else:
        ch = l[index][2]
        w = []
        for c in ch:
            w.append(get_total_weight(l,c))
        if all(w[i] == w[i+1] for i in range(0, len(w)-1)):
            return l[index][1] + sum(w)
        else:
            for k,v in enumerate(w):
                if w.count(v) == 1:
                    print 'part 2:', l[l[index][2][k]][1] - (max(w)-min(w))
                    sys.exit(0)

lines = open('7.txt', 'r').readlines()
parents = [-1]*len(lines)
nodes = []
# populate nodes list
for line in lines:
    parts = line.split()
    parts[1] = int(parts[1].replace('(','').replace(')',''))
    nodes.append([parts[0],parts[1],[]])

# populate parent of each node
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
get_total_weight(nodes, parents.index(-1))