def packet_will_hit_scanner(layer, size, delay=0):
    if size == 1:
        return True
    return (layer + delay) % (2 * size - 2) == 0


def get_severity(lines):
    total = 0
    for depth, length in lines:
        if packet_will_hit_scanner(depth, length):
            total += depth * length
    return total


layers = [map(int, line.replace(':', '').split()) for line in open('13.txt', 'r').readlines()]

print 'part 1:', get_severity(layers)

# 4.54 sec, could be worse
i = 0
while any(packet_will_hit_scanner(x, y, i) for x, y in layers):
    i += 1
print 'part 2:', i
