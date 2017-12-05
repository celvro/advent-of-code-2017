input = 265149

ring = 1
br_corner = 1
row_length = 1

while br_corner < input:
    ring += 1
    row_length = ring*2-1
    br_corner = row_length**2

corners = [br_corner-(row_length-1)*i for i in range(0, ring+2)]
dist_from_corner = min([abs(c - input) for c in corners])

print('part 1:', row_length-1 - dist_from_corner)

# initialize variables for first square
num_list = [1,1,2,4,5,10,11,23,25]
i = 8
turns = 3
dist = 3
next_corner = 9
while num_list[i] < input:
    i+=1
    new_num = num_list[i-1]
    if(i == next_corner):
        turns += 1
        new_num += num_list[i - turns*2]
        if(turns%2):
            dist += 1
        next_corner += dist
    elif(next_corner - dist == i-1):
        new_num += num_list[i - turns*2]
        new_num += num_list[i - (turns*2+1)]
        new_num += num_list[i-2]
    elif(next_corner - i == 1):
        new_num += num_list[i - (turns*2+1)]
        new_num += num_list[i - (turns*2+2)]
    else:
        new_num += num_list[i - (turns*2)]
        new_num += num_list[i - (turns*2+1)]
        new_num += num_list[i - (turns*2+2)]
    num_list.append(new_num)

print('part 2:', num_list[-1])