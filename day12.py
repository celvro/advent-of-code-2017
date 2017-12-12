from collections import defaultdict


def recursive_add_to_set(k, tmp_set):
    if k not in checked:
        checked.add(k)
        tmp_set.add(k)
        for p in m[k]:
            recursive_add_to_set(p, tmp_set)
    return tmp_set


m = defaultdict(list)

for line in open('12.txt', 'r').readlines():
    numbers = [int(s) for s in line.replace(',', '').split() if s[0].isdigit()]
    m[numbers[0]] = numbers

checked = set()
groups = list()
for key in m.keys():
    tmp = set()
    if len(recursive_add_to_set(key, tmp)) > 0:
        groups.append(tmp)

print 'part 1:', len([g for g in groups if 0 in g][0])
print 'part 2:', len(groups)
