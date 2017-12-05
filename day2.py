# return all factors not including 1 and itself
def factors(n):
    x = []
    i = 2
    while i*i <= n:
        if not n%i:
            x.extend((i, n//i))
        i+=1
    return list(set(x))

f = open('2.txt', 'r')

sum = 0
sorted_input = []
for line in f.readlines():
    nums = [int(i) for i in line.split()]
    sorted_input.append(sorted(nums, reverse=True))
    sum += max(nums) - min(nums)
print('part 1:', sum)

sum = 0
for row in sorted_input:
    for num in row:
        for i in factors(num):
            if i in row:
                sum += num//i
                break
print('part 2:', sum)