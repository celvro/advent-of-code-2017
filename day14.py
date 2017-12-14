from math import sqrt
from day10 import knot_hash


def add_neighbors(index, group, global_checked, arr):
    """Add neighbors of index to group if not already checked"""
    # could also pass length in if array is not square
    length = int(sqrt(len(arr)))
    up = index - length
    right = index + 1
    down = index + length
    left = index - 1

    def recursive_add(direction, grp, chk):
        chk.add(direction)
        if arr[direction] == '1':
            grp.append(direction)
            grp, chk = add_neighbors(direction, grp, chk, arr)
        return grp, chk

    if up > 0 and up not in global_checked:
        group, global_checked = recursive_add(up, group, global_checked)
    if index % length != length - 1 and right not in global_checked:
        group, global_checked = recursive_add(right, group, global_checked)
    if down < length * length and down not in global_checked:
        group, global_checked = recursive_add(down, group, global_checked)
    if index % length != 0 and left not in global_checked:
        group, global_checked = recursive_add(left, group, global_checked)
    return group, global_checked


if __name__ == '__main__':
    key = 'jzgqcdpd'
    knot_hashes = [knot_hash(key + '-' + str(i)) for i in range(0, 128)]
    bin_hashes = ["{:0128b}".format(int(s, 16)) for s in knot_hashes]
    joined_hashes = "".join(bin_hashes)

    groups = list()
    checked = set()
    for k, v in enumerate(joined_hashes):
        if k not in checked and v == '1':
            new_group = [k]
            new_group, checked = add_neighbors(k, new_group, checked, joined_hashes)
            groups.append(new_group)

    print 'part 1:', joined_hashes.count('1')
    print 'part 2:', len(groups)
