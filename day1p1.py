def krotki(l):
    for i in range(1, 2021):
        l.append([i, 2020-i])
possible=[]
given=[]
krotki(possible)
f=open("inpu.txt", "r")
for line in f:
    given.append(int(line))
for pair in possible:
        if pair[0] in given and pair[1] in given:
            print(pair[0]*pair[1])
f.close()