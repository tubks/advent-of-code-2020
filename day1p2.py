def krotki(l):
    for i in range(1, 2021):
        for j in range(1, 2020-i):
            l.append([i, j, 2020-i-j])
possible=[]
given=[]
krotki(possible)
f=open("inpu.txt", "r")
for line in f:
    given.append(int(line))
for pair in possible:
       if (pair[0] in given and pair[1] in given and pair[2] in given):
           result=pair[0]*pair[1]*pair[2]
           print(result)
f.close()