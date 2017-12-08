#day6.py
def redistribute(nums):
    max_index, max_val = max(enumerate(nums), key=lambda x: x[1])
    to_add = max_val // len(nums)
    remainder = max_val % len(nums)
    nums[max_index] = 0
    nums = [n + to_add for n in nums]
    for i in range(1, remainder+1):
        j = i
        if max_index+j >= len(nums): j -= len(nums)
        nums[max_index+j] += 1
    return nums

steps = []
next = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
key = ''.join(map(str, next))
while key not in steps:
    steps.append(key)
    next = redistribute(next)
    key = ''.join(map(str, next))
print 'part 1:', len(steps)
print 'part 2:', len(steps) - steps.index(key)