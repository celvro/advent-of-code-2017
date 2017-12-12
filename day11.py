# https://www.redblobgames.com/grids/hexagons/#neighbors
directions = dict(nw=(0, 1, -1), n=(1, 0, -1), ne=(1, -1, 0), se=(0, -1, 1), s=(-1, 0, 1), sw=(-1, 1, 0))


def get_dist(a, b):
    return max(abs(a[0] - b[0]), abs((a[1] - b[1])), abs(a[2] - b[2]))


furthest = 0
pos = [0, 0, 0]
for d in open('11.txt', 'r').read().strip().split(','):
    move = directions[d]
    pos = [x + y for x, y in zip(pos, move)]
    furthest = max(furthest, get_dist(pos, (0, 0, 0)))

print 'part 1:', get_dist(pos, (0, 0, 0))
print 'part 2:', furthest
