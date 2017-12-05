f = open('4.txt', 'r')

count1 = 0
count2 = 0
for line in f.readlines():
    words = line.split()
    if len(words) == len(set(words)):
        count1+=1
    words2 = map(''.join, map(sorted, words))
    if len(words2) == len(set(words2)):
        count2+=1
print('part 1:', count1)
print('part 2:', count2)