# input = open('10.txt', 'r').read().split()
inp = [31, 2, 85, 1, 80, 109, 35, 63, 98, 255, 0, 13, 105, 254, 128, 33]
arr = range(0, 256)
curr_pos = 0
skip_size = 0

for length in inp:
    end = (length + curr_pos - 1) % len(arr)
    if end < curr_pos:
        tmp = arr[curr_pos:] + arr[:end + 1]
    else:
        tmp = arr[curr_pos:end + 1]
    tmp = tmp[::-1]
    for i in range(0, length):
        j = (curr_pos + i) % len(arr)
        arr[j] = tmp[i]
    curr_pos = (curr_pos + length + skip_size) % len(arr)
    skip_size += 1
print 'part 1:', arr[0] * arr[1]
