f = open("inpu3.txt", "r")
pattern = []
tree_counter = 0
for line in f:
    line = line.replace("\n", "")
    pattern.append(line)
print(pattern)
position = [0, 0]
for i in range(1, len(pattern)):
    position[0] += 1
    position[1] += 3
    check = pattern[position[0]][(position[1]) % (len(pattern[i]))]
    if check == "#":
        tree_counter += 1
print(tree_counter)
