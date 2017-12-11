ignore_next = False
is_garbage = False
level = 0
total = 0
garbage_cnt = 0
for c in open('9.txt', 'r').read():
    if ignore_next:
        ignore_next = not ignore_next
    elif is_garbage:
        if c == '!':
            ignore_next = True
        elif c == '>':
            is_garbage = False
        else:
            garbage_cnt += 1
    elif c == '<':
        is_garbage = True
    elif c == '{':
        level += 1
        total += level
    elif c == '}':
        level -= 1
print 'part 1:', total
print 'part 2:', garbage_cnt
