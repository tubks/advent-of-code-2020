#task 1
from math import floor, ceil
passes=[]
seats=[]
row_min=0
row_max=127
row_found=-1
col_min=0
col_max=7
col_found=-1
f=open("inpu5.txt", "r")
for line in f:
    passes.append(line)
for seat in passes:
    for letter in seat:
        if letter=="F":
            row_max=floor(row_min+((row_max-row_min)/2))
        elif letter=="B":
            row_min=ceil(row_min+((row_max-row_min)/2))
        elif letter=='L':
            col_max = floor(col_min+((col_max-col_min) / 2))
        elif letter=='R':
            col_min = ceil(col_min+((col_max-col_min) / 2))
        if row_min==row_max:
            row_found=row_max
        if col_max==col_min:
            col_found=col_max
    seat=col_found+8*row_found
    seats.append(seat)
    row_min = 0
    row_max = 127
    row_found = -1
    col_min = 0
    col_max = 7
    col_found = -1
#part 2
seats=set(seats)
possible_seats=set(range(1024))
free=possible_seats.difference(seats)
for seat in free:
    if seat-1 in seats and seat+1 in seats:
        print(seat)